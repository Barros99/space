from django import forms


class LoginForms(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=100)
    password = forms.CharField(
        label="Password",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(),
    )
