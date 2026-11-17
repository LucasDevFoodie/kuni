from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)

    email = forms.EmailField()

    telephone = forms.CharField(
        max_length=30,
        required=False,
    )

    message = forms.CharField(
        widget=forms.Textarea,
    )