# polls/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

class UsernameOrEmailBackend(ModelBackend):
    """
    Custom authentication backend that allows users to log in with either username or email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try to fetch the user by email if the username isn't found
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # Try to fetch by username if not found by email
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        
        # Check if the password matches
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
