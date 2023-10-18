from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'photo', 'date_of_birth']
