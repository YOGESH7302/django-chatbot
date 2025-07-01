from django.contrib import admin
from django.urls import path
from chatbot.views import chat

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", chat),
]

