from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from DoLis.core.models import Question, Event

UserModel = get_user_model()


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('body',)
        widgets = {'body': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Type your question here',
                                                 'rows': 3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = ''


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }))

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }))

    class Meta:
        model = UserModel


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

    username = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   }))

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   }))

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   }))

    class Meta:
        model = UserModel
        fields = ('username', 'password1', 'password2')


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'code', 'description')
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'code': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
        }