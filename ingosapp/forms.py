from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length = 100, required = True,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Full name'
                           }))
    email = forms.EmailField(max_length = 300, required = True,
                           widget=forms.TextInput(attrs={
                               'placeholder': 'Email'
                           }))
    subject = forms.CharField(max_length = 300, required = True,
                           widget=forms.Textarea(attrs={
                               'placeholder': 'Subject'
                           }))
    message = forms.CharField(max_length = 5000, required = True,
                           widget=forms.Textarea(attrs={
                               'placeholder': 'Message',
                               'rows': "8"
                           }))

    class Meta:
        model = ContactProfile
        fields = ('name', "email", "subject", "message")