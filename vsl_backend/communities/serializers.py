from rest_framework import serializers
from .models import *

class CommunitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Community
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'

class ReactionSerializer(serializers.ModelSerializer):
    content_type = serializers.ReadOnlyField(source="content_type.name")
    object_id = serializers.ReadOnlyField()
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Reaction
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Page
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    
    class Meta:
        model = Comment
        fields = '__all__'
