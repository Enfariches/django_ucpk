from django.db import models

class File(models.Model):
    title = models.CharField(max_length= 200)
    pdf = models.FileField()

    def __str__(self):
        return self.title
