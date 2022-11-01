from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from brokentv.accounts.models import BrokenTvUser
from brokentv.web.validators import validator_profile_username, validator_profile_name_only_letters

UserModel = get_user_model()


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
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.username


class Tag(models.Model):
    TAG_MAX_LEN = 50

    name = models.CharField(
        max_length=TAG_MAX_LEN,
        unique=True,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    TITLE_MAX_LEN = 240
    SUBTITLE_MAX_LEN = 240
    SLUG_MAX_LEN = 250

    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )

    subtitle = models.CharField(
        max_length=SUBTITLE_MAX_LEN,
    )

    slug = models.SlugField(
        max_length=SLUG_MAX_LEN,
        unique=True,
    )

    body = models.TextField()

    meta_description = models.CharField(
        max_length=150,
        unique=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    last_modified = models.DateTimeField(
        auto_now=True,
    )

    publish_date = models.DateTimeField(
        blank=True,
        null=True,
    )

    published = models.BooleanField(default=False)

    author = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
    )



