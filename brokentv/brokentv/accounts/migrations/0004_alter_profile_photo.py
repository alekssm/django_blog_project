# Generated by Django 4.1.2 on 2022-11-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='default_user_profile.png', upload_to='profile/'),
        ),
    ]
