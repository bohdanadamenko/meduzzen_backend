from django.contrib import admin
from Quizzes.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ['username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
