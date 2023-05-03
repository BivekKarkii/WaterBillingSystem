from django.contrib.auth.backends import BaseBackend

from consumer.models import Consumer_Profile


class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, phone=None, password=None, **kwargs):
        try:
            user = Consumer_Profile.objects.get(phone=phone)
        except Consumer_Profile.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return Consumer_Profile.objects.get(pk=user_id)
        except Consumer_Profile.DoesNotExist:
            return None
