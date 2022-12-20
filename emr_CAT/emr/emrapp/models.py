from django.db import models

# Create your models here.
class records(models.Model):
    Name = models.CharField(max_length=100)
    Doctor = models.CharField(max_length=100)

    def __str__(self):
        return self.Name, self.Doctor