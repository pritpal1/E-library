from django.db import models
from django.utils import timezone
# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    pulish_date=models.DateField(default=timezone.now)
    price=models.IntegerField(default=0)
    def __str__(self):
        return self.name + ' by '+ self.author
