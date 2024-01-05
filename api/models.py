from django.db import models

# Create your models here.


class File(models.Model):
    choice = (
        ('latin', 'latin'),
        ('cyrillic', 'cyrillic')
    )
    file = models.FileField(upload_to='files', blank=True)
    pattern = models.CharField(max_length=20, choices=choice)

    def __str__(self):
        return self.file
