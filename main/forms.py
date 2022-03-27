from django import forms
from . import models


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = [
            "name",
            "email",
            "text"
        ]
        labels = {
            "name": "",
            "email": "",
            "text": ""
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "fill__input", "placeholder": "NAMN"}),
            "email": forms.TextInput(attrs={"class": "fill__input", "placeholder": "EMAIL"}),
            "text": forms.TextInput(attrs={"class": "fill__text", "placeholder": "MEDDELANDE"}),
        }
