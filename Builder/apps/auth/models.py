from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from rest_framework_jwt.settings import api_settings

# JWT Payload
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_setting.JWT_ENCODE_HANDLER


class UserManager(BaseUserManager):
    # BaseUserManager has normalize email and get random password

    def create_user(self,username,email=None,password, first_name=None, last_name=None):
        if username is None:
            raise TypeError('Username is required')
        if password is None:
            raise TypeError('You need a password!')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_staff=False,
        )
        # Takes care of password hashing but is at the db level, so hash beforehand
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,email,password):
        # Admin permissions
        if password is None:
            raise TypeError('Passwords area must')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """
    AbstractBAseUser has the required fields option as well others such as the password, is active, and last login  

    Permission Mixin has the superuser field and permissions functions
    """
    username = models.CharField(db_index=True, max_length=200, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.username
    
    # 
    @property
    def token(self):
        return self._genetate_jwt_token()

    def _genetate_jwt_token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token

        