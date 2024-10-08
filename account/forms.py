from django import forms
from django.contrib.auth.models import User

# login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control smf border-0 border-bottom border-2 border-warning border-opacity-50 rounded-0'
                }
            )
        self.fields['username'].widget.attrs.update(
            {
                'placeholder': 'اسم المستخدم'
            }
        )
        self.fields['password'].widget.attrs.update(
            {
                'placeholder': 'كلمة المرور'
            }
        )

# register form
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control fnt border-0 border-bottom rounded-0'
                }
            )
