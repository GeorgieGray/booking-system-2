from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

# credit: https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username/
class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **rest):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **rest)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **rest):
        rest.setdefault('is_staff', True)
        rest.setdefault('is_superuser', True)

        if rest.get('is_staff') is not True:
            raise ValueError('Superusers must have is_staff')
        
        if rest.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser')

        return self._create_user(email, password, **rest)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()