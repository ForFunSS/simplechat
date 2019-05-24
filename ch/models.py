from django.db import models

class Textes(models.Model):
    chat_user = models.CharField(max_length=30)
    chat_text = models.CharField(max_length=1000)

    def __str__(self):
        return '%s %s' % (self.chat_user, self.chat_text)
