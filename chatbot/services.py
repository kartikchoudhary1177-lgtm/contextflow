from google import genai
from django.conf import settings
import re
from io import BytesIO
from PIL import Image
import os
from django.conf import settings
from huggingface_hub import InferenceClient

# Gemini client for text generation
client = genai.Client(api_key=settings.GEMINI_API_KEY)

TEXT_MODEL = "gemini-2.5-flash"


def build_context(conversation, limit=6):
    msgs = conversation.messages.order_by("-created_at")[:limit]
    return "\n".join(
        f"{m.sender.upper()}: {m.text}" for m in reversed(msgs) if m.text
    )


def generate_text_reply(user_message, context):
    prompt = f"""
      You are a helpful contextual chatbot.
      Conversation history:
     {context}
      User message: {user_message}
      Give a short answer. """

    response = client.models.generate_content(
        model=TEXT_MODEL,
        contents=prompt
    )

    return response.text.strip()


import requests
from django.conf import settings

def generate_image_reply(user_message, context):
    """
    Generate an image with Hugging Face and save it in Django media folder.
    Returns a browser-usable URL like /media/generated_xxx.png
    """

    prompt = user_message.strip()
    if not prompt:
        return None

    client = InferenceClient(api_key=settings.HUGGINGFACE_API_KEY)

    try:
        # Pick a commonly available text-to-image model.
        # You can later try:
        # "black-forest-labs/FLUX.1-schnell"
        # "stabilityai/stable-diffusion-xl-base-1.0"
        image = client.text_to_image(
            prompt,
            model="black-forest-labs/FLUX.1-schnell"
        )

        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)

        safe_name = re.sub(r"[^a-zA-Z0-9_-]+", "_", prompt[:30]).strip("_")
        if not safe_name:
            safe_name = "image"

        file_name = f"generated_{safe_name}.png"
        file_path = os.path.join(settings.MEDIA_ROOT, file_name)

        if isinstance(image, Image.Image):
            image.save(file_path, format="PNG")
        else:
            # Fallback if provider returns bytes-like content
            img = Image.open(BytesIO(image))
            img.save(file_path, format="PNG")

        return f"{settings.MEDIA_URL}{file_name}"

    except Exception as e:
        print("Hugging Face image generation error:", str(e))
        return None