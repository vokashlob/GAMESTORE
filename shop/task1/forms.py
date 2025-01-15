from django import forms


class RegisterForm(forms.Form):
    login = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Введите пароль:')
    password_repeat = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.CharField(max_length=3, label='Введите свой возраст')
