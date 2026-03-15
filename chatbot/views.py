from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer, ChatRequestSerializer
from .services import build_context, generate_text_reply, generate_image_reply

# Create your views here.

class ConversationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        conversations = Conversation.objects.filter(user=request.user).order_by("-updated_at")
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get("title", "")
        conversation = Conversation.objects.create(user=request.user, title=title)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConversationMessagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        conversation = get_object_or_404(Conversation, id=id, user=request.user)
        messages = conversation.messages.order_by("created_at")
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


class ChatView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChatRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        conversation = get_object_or_404(Conversation,id=serializer.validated_data["conversation_id"],user=request.user )

        user_message_text = serializer.validated_data["message"]
        mode = serializer.validated_data["mode"]

        Message.objects.create( conversation=conversation, sender="user", mode=mode,text=user_message_text )
        
        context = build_context(conversation)
        
        if mode == "text":
            bot_reply = generate_text_reply(user_message_text, context)

            Message.objects.create(conversation=conversation,sender="bot",mode="text",text=bot_reply )

            response_data = {
                "question": user_message_text,
                "answer": bot_reply
            }

        
        else:
            image_url = generate_image_reply(user_message_text, context)

            Message.objects.create(conversation=conversation,sender="bot",mode="image",text=f"Generated image for: {user_message_text}",image_url=image_url )

            response_data = {
                "question": user_message_text,
                "image_url": image_url
            }

        return Response(response_data, status=status.HTTP_200_OK)