from django import forms

from brokentv.web.models import Profile


# class CreateProfileFrom(forms.ModelForm):
#     class Meta:
#         model = Profile
#         exclude = ('user', )

# class EditProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('email', 'username', 'password', 'first_name', 'last_name', 'age',)