from django import forms

class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form__input", "placeholder": "Логин"}), required=True, label='Введите имя')
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form__input", "placeholder": "Почта"}), required=True, label='Введите почту')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder": "Пароль"}), required=True, label='Введите пароль')

class SignForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form__input", "placeholder": "Логин"}), required=True, label='Введите имя')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form__input", "placeholder": "Пароль"}), required=True, label='Введите пароль')
