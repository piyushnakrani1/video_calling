from django.urls import path, re_path

from core import consumers

websocket_urlpatterns = [
    re_path(r'user/', consumers.ChatConsumer.as_asgi()),
]