from Companies.models import Company
from Quizzes.models import CustomUser

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Specifies the model to be serialized
        fields = '__all__'  # Specifies that all fields in the model should be serialized
        # Password field should be write-only to maintain security
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Overrides the default create method to handle user creation.
        It creates a user instance and sets the password.
        """
        password = validated_data.pop(
            'password')  # Extracts password from validated data
        # Creates user with all provided fields
        user = CustomUser.objects.create(**validated_data, is_active=False)
        user.set_password(password)  # Hashes and sets the password
        user.save()  # Saves the user instance
        return user  # Returns the created user instance

    def update(self, instance, validated_data):
        """Overrides the default update method to handle user update.
        If a password is provided, it hashes the password before saving.
        """
        password = validated_data.pop(
            'password', None)  # Extracts password from validated data if it exists
        if password:  # If password is provided
            instance.set_password(password)  # Hashes and sets the new password
        # Calls the parent class's update method and returns the updated instance
        return super().update(instance, validated_data)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'owner',
                  'is_visible', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'owner']


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description',
                  'is_visible', 'created_at', 'updated_at']
