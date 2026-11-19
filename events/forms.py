from django import forms
from .models import Event, Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'event_date',
            'location',
            'category',
            'is_published',
            'capacity',
        ]
        widgets = {
            'event_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['attendee_name', 'attendee_email', 'comments']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]