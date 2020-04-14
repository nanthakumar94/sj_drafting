from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    company_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(required=True)
    project = forms.CharField(widget=forms.Textarea, required=True)


