from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.name + " | " + self.email