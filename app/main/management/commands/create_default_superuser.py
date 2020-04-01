import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user_model = get_user_model()
        user_name = os.getenv('DJANGO_USER_NAME')
        user_email = os.getenv('DJANGO_USER_EMAIL')
        user_password = os.getenv('DJANGO_USER_PASSWORD')
        user = user_model.objects.filter(username=user_name).first()
        if not user:
            user = user_model()
        user.username = user_name
        user.user_email = user_email
        user.is_superuser = True
        user.is_staff = True
        user.set_password(user_password)
        user.save()
