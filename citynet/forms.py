from django import forms
from .models import GetInTouch

class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control ',
            'name': 'name',
            'id': 'name',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Enter your full name"',
            'placeholder': ' Enter your full name'

        })
        self.fields['phone_number'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control ',
            'name': 'phone',
            'id': 'phone',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Enter phone number"',
            'placeholder': ' Enter phone number'
        })
        self.fields['message_subject'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'name': 'subject',
            'id': 'subject',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Enter Subject"',
            'placeholder': ' Enter Subject'
        })
        self.fields['message_text'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'message',
            'id': 'message',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Enter Message"',
            'placeholder': ' Enter Message',
            'cols': '30',
            'rows': '9'
        })

class GetInTouchBoolen(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ('read_or_not', )
