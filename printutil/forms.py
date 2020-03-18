from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import PrintRequest

class PrintRequestForm(forms.ModelForm):
    class Meta:
        model = PrintRequest
        fields = ('source',)
        widgets = {
            'source': forms.FileInput(
                attrs={
                    'class': 'custom-file-input',
                    'id': 'file',
                }
            )
        }

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mb-2',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control mb-2',
        }
    ))