from django import forms
from models import Textes

class TextesForm(forms.Form):
    chat_user = models.CharField(max_length=30)
    chat_text = models.CharField(max_length=1000)

    def save(self):
        new_message = Textes.objects.create(
            chat_user=self.cleanned_data['chat_user'],
            chat_text=self.cleanned_data['chat_text']
        )
        return new_message
