from django.db import models

# Create your models here.
from django.db import models
from user_auth.models import User


class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="conversations")
    title = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or f"Conversation {self.id}"


class Message(models.Model):
    MODE_CHOICES = (
        ("text", "Text"),
        ("image", "Image"),
    )

    SENDER_CHOICES = (
        ("user", "User"),
        ("bot", "Bot"),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name="messages")
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    text = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.mode}"