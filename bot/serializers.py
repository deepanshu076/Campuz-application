from rest_framework import serializers
from .models import ChatMessage, FAQ

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'message', 'response', 'timestamp']
        read_only_fields = ['id', 'timestamp']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'category']
