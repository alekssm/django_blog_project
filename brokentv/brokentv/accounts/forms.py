from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from brokentv.web.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=Profile.USERNAME_MAX_LENGTH,
    )

    class Meta:
        model = UserModel
        fields = ["email", ]

    def clean_username(self):
        return self.cleaned_data['username']

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(username=self.clean_username(),
                          user=user,
                          )

        if commit:
            profile.save()
        return user




