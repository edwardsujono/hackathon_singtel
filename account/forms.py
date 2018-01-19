from django import forms

from .models import Account


class PostForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('name', 'email')
