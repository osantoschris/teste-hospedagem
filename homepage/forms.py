from django import forms
from .models import ContactMe

class ContactMeForm(forms.ModelForm):

    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'message', 'subject']

    def __init__(self, *args, **kargs):
        super().__init__(*args, *kargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'