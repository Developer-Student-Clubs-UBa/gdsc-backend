from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Social


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class SocialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Social
        fields = ['userid', 'blog', 'github', 'linkedin', 'twitter', 'portfolio']
