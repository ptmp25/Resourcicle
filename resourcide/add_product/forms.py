from django import forms

class NameForm(forms.Form):
    name = forms.CharField(
        max_length=20,  # Adjust the maximum length as needed.
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Name', 'required': True}),
        # Add any additional validation rules here.
    )


class DescriptionForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea(attrs={'class' : 'description-input'}))