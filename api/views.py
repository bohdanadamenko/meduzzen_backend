import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from Quizzes.models import CustomUser
from .serializers import UserSerializer
from django.http import Http404
from .permissions import IsOwnerOrAdmin
from pydantic import BaseModel, ValidationError



logger = logging.getLogger(__name__)


class CustomUserPydantic(BaseModel):
    username: str
    password: str


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]

    def create(self, request, *args, **kwargs):
        try:
            CustomUserPydantic(**request.data)
            response = super().create(request, *args, **kwargs)
            if response.status_code == status.HTTP_201_CREATED:
                logger.info(f"User created: {response.data}")
            return response
        except ValidationError as e:
            error_messages = e.errors()  # Extract error messages from the ValidationError
            return Response({'error': 'Invalid input', 'details': error_messages}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            if response.status_code == status.HTTP_200_OK:
                logger.info(f"User updated: {response.data}")
            return response
        except Http404:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            user_data = self.get_serializer(instance).data
            response = super().destroy(request, *args, **kwargs)
            logger.info(f"Response status code: {response.status_code}")
            if response.status_code == status.HTTP_204_NO_CONTENT:
                print('test')
                logger.info(f"User deleted: {user_data}")
            return response
        except Http404:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)