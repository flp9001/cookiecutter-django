from __future__ import unicode_literals

from django import forms
from django.utils import translation
from betterforms.multiform import MultiModelForm

from .models import User, UserProfile


class SignupForm(forms.Form):

    def signup(self, request, user):
        user.save()
        language = translation.get_language_from_request(request, check_path=True)
        user.profile.language = language
        user.profile.save()


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'username')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthday', 'language')

class UserEditMultiForm(MultiModelForm):
    form_classes = {
        'user': UserEditForm,
        'profile': UserProfileForm,
    }
