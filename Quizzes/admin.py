from Companies.models import Company
from Quizzes.models import CustomUser

from django.contrib import admin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['username', 'email']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at', 'updated_at', 'owner')
