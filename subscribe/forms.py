from faulthandler import disable
from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe
# the variable names, such as first_name, will be rendered as the form 
# labels: eg first_name renders as the label First name.
# And the html table cell will have the identify id_first_name.

def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("Invalid entry")
    return value

# see how model field is converted to a form field
# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#field-types

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        # fields=['first_name', 'last_name', 'email']
        # exclude = ('first_name',)
        fields = '__all__'
        labels={
            'first_name':_('Preferred first name or sobriquet'),
            'email':_('Email (required)')
        }
        help_texts={'last_name':_('Not required')}