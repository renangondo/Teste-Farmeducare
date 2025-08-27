from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UsuarioCadastroForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control"}
        ),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já existe.")
        return username
