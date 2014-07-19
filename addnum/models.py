from django.db import models
from django import forms

# Create your models here.

class NumbersForm(forms.Form):
	num1 = forms.IntegerField('First Number')
	num2 = forms.IntegerField('Second Number')
#	answer = forms.IntegerField(required=False)
