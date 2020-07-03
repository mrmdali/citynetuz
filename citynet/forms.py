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
            'onblur': 'this.placeholder = "Введите свое полное имя"',
            'placeholder': ' Введите свое полное имя'

        })
        self.fields['phone_number'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control ',
            'name': 'phone',
            'id': 'phone',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Введите номер телефона"',
            'placeholder': ' Введите номер телефона'
        })
        self.fields['message_subject'].widget.attrs.update({
            'type': 'text',
            'class': 'form-control',
            'name': 'subject',
            'id': 'subject',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Введите тему"',
            'placeholder': ' Введите тему'
        })
        self.fields['message_text'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'message',
            'id': 'message',
            'onfocus': 'this.placeholder = ""',
            'onblur': 'this.placeholder = "Введите сообщение"',
            'placeholder': ' Введите сообщение',
            'cols': '30',
            'rows': '9'
        })

class GetInTouchBoolen(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ('read_or_not', )
