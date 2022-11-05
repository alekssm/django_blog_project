from django.contrib.auth import get_user_model
from django.db import models
from brokentv.accounts.models import BrokenTvUser


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
        ordering = ["-date_created"]

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

    # publish_date = models.DateTimeField(
    #     blank=True,
    #     null=True,
    # )
    #
    # published = models.BooleanField(default=False)

    author = models.ForeignKey(
        BrokenTvUser,
        on_delete=models.PROTECT,
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title



