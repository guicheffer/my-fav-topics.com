from rest_framework import serializers
from .models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        # field = '__all__'
