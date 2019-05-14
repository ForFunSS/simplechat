from django.db import models

class Text(models.Model):
    chat_user = models.CharField(max_length=30)
    chat_text = models.CharField(max_length=2000)


    def __str__(self):
        return self.chat_user

    def __str__(self):
        return self.chat_text
