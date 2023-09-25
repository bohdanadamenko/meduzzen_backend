from rest_framework import serializers
from Quizzes.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'  # What we need to serialized
