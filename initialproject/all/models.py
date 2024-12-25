from django.db import models
from django.utils import timezone

class Chaivariety(models.Model):
    CHAI_TYPE_CHOICE =[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('PL','PLAIN'),

    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
     





# Create your models here.
