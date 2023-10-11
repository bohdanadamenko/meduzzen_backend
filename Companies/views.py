from api.permissions import IsOwnerOrAdmin
from api.serializers import CompanyListSerializer, CompanySerializer

from .models import Company

from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination


class CompanyCreateView(generics.CreateAPIView):
    """
    Handle company creation.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the owner (user who created the company) along with the company.
        """
        serializer.save(owner=self.request.user)


class CompanyListView(generics.ListAPIView):
    """
    List all companies for authenticated users.
    """
    queryset = Company.objects.all()
    # Assuming you have different serializer for listing
    serializer_class = CompanyListSerializer
    permission_classes = [permissions.IsAuthenticated]
    # Pagination is applied automatically from global settings
    pagination_class = PageNumberPagination


class CompanyManageView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handle the retrieve, update, or delete operations for a company.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsOwnerOrAdmin]
