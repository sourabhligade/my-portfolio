from django.db import models

# Create your models here.

class Project(models.Model):
    title=models.CharField(max_length=343)
    description=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='projectimages/')

    def __str__(self) -> str:
        return self.title   