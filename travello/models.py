from django.db import models

# Create your models here.

class Destination(models.Model):
    
    name = models.CharField(max_length = 100)
    img= models.ImageField(upload_to = 'pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name 

class Discount(models.Model):
    
    subtitle = models.CharField(max_length = 100)
    discount = models.IntegerField()

    def __str__(self):
        return self.subtitle 

    
class Testimonials(models.Model):
    
    testimonial = models.CharField(max_length = 100)
    client = models.CharField(max_length = 100)
    client_profession = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.client} - {self.testimonial}" 

