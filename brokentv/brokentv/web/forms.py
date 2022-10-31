from django import forms

from brokentv.web.models import Profile


class CreateProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )