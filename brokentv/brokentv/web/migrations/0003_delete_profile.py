# Generated by Django 4.1.2 on 2022-11-05 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_tag_profile_bio_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
