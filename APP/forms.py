from django import forms
from .crud import *
from .models import *


class SomeForm(forms.Form):
    CHOICES = TYPES
    picked = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple())
