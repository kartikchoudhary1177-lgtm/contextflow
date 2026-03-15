from google import genai
from django.conf import settings

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


def generate_image_reply(user_message, context):
    # Free AI image generation
    image_url = f"https://image.pollinations.ai/prompt/{user_message.replace(' ', '%20')}"
    return image_url