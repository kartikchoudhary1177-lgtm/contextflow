from django.contrib import admin
from django.urls import path,include
from chatbot.views import ConversationCreateView,ConversationMessagesView,ChatView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('conversation/',ConversationCreateView.as_view()),
    path('message<id>/',ConversationMessagesView.as_view()),
    path('chat/',ChatView.as_view(),name = "chat")
]
