from django import forms
from django.forms import ModelForm
from .models import Trial


class MapForm(ModelForm):
    class Meta:
        model = Trial
        fields = ['place']

    def __init__(self, *args, **kwargs):
        super(MapForm, self).__init__(*args, **kwargs)
        self.fields['place'].widget = forms.TextInput(
            attrs={'id': 'google-place-auto-compete'})
