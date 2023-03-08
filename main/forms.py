from django import forms
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(max_length=400, widget=forms.Textarea)