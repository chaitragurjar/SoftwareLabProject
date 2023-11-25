from django.db import models
# Create your models here.

class Image(models.Model):
    Song_Name=models.CharField(max_length=100)
    Upload_File=models.FileField(upload_to=".")
    def __str__(self):
        return self.Song_Name