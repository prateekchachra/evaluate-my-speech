from django.db import models


class SpeechPost(models.Model):
    speech_title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')
    url_youtube = models.URLField
    url_google_docs = models.URLField
    speech_add_text = models.CharField(max_length=1000)
    #TODO : Enum for type
    #TODO : Include competition speeches
    #TODO : Boolean for public/private