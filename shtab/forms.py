from django import forms
from django.core.exceptions import ValidationError

from .models.Poruchenie import Poruchenie

class NewPoruchenieForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Poruchenie
        fields = '__all__'
        # widgets = {
        #     'otv': forms.TextInput(attrs={'class': 'form-input'}),
        #     'por': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        # }
    #
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError('Длина превышает 200 символов')

        # return title
