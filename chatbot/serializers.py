from rest_framework import serializers
from .models import Conversation, Message


class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "title", "created_at", "updated_at"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "conversation", "sender", "mode", "text", "image_url", "created_at"]


class ChatRequestSerializer(serializers.Serializer):
    conversation_id = serializers.IntegerField()
    message = serializers.CharField()
    mode = serializers.ChoiceField(choices=["text", "image"])