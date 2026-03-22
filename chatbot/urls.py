from django.contrib import admin
from django.urls import path,include
from chatbot.views import ConversationCreateView,ConversationMessagesView,ChatView
from .views import auth_page
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('conversation/',ConversationCreateView.as_view()),
    path('conversation/<id>/message/',ConversationMessagesView.as_view()),
    path('chat/',ChatView.as_view(),name = "chat"),
    path("", auth_page, name="auth_page"),
    path("conversation/<int:id>/", ConversationCreateView.as_view(), name="delete_conversation"),
    path("chat/", ChatView.as_view(), name="chat"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

