from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
class Chai_Review (models.Model):
    chai = models.ForeignKey(Chaivariety, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    comment = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
#many to many models
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_variety = models.ManyToManyField(Chaivariety,related_name='stores')


    
    def __str__(self):
        return self.name
    
#one to one
class Chai_certificate(models.Model):
    chai = models.OneToOneField(Chaivariety, on_delete=models.CASCADE,related_name='certificate')
    issued_date = models.DateField(default=timezone.now)
    validity_date = models.DateField(default=timezone.now)
    def __str__(self):
        return f"{self.chai.name}"
