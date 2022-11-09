from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from brokentv.accounts.managers import BrokenTvUsersManager
from brokentv.web.validators import validator_profile_username, validator_profile_name_only_letters


class BrokenTvUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = BrokenTvUsersManager()


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2

    FIRST_NAME_MAX_LENGTH = 25
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 25
    LAST_NAME_MIN_LENGTH = 2

    AGE_MIN_VALUE = 0

    BIO_MAX_LEN = 240

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validator_profile_username,
        ),
        # unique=True,
    )

    photo = models.ImageField(
        default='default_user_profile_image.png',
        upload_to='profile/',
        null=False,
        blank=True,
    )

    bio = models.CharField(
        max_length=BIO_MAX_LEN,
        blank=True,
        null=True,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validator_profile_name_only_letters,
        ),
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validator_profile_name_only_letters,
        ),
        blank=True,
        null=True,
    )

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )

    user = models.OneToOneField(
        BrokenTvUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.username
