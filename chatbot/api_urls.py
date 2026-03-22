from django.urls import path
from .views import ConversationCreateView, ConversationMessagesView, ChatView

urlpatterns = [
    path("conversations/", ConversationCreateView.as_view(), name="conversations"),
    path("conversations/<int:id>/messages/", ConversationMessagesView.as_view(), name="conversation_messages"),
    path("chat/", ChatView.as_view(), name="chat"),
]