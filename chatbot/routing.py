# chatbot/routing.py
from django.urls import path
from .consumers import ChatConsumer  # ✅ This must match the filename

websocket_urlpatterns = [
    path("ws/chat/", ChatConsumer.as_asgi()),
]
