from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(required=True, max_length=255)
