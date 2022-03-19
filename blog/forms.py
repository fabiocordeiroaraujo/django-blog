from django import forms
from django.utils.translation import gettext_lazy

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": gettext_lazy("your_name")
        })
    )
    email = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": gettext_lazy("email")
        })
    )
    body = forms.CharField(
        widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": gettext_lazy("deixe_comentatio")
        })
    )
