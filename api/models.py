from django.db import models

# Create your models here.


#Creating Company Model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    type = models.CharField(max_length=255,choices=(('IT','IT'),('Non IT','Non IT'),('Mobile Phones','Mobile Phones')))
    added_date = models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    upload = models.ImageField(upload_to ='api_images',null=True,blank=True) 
    
    def __str__(self):
        return self.name
    
    
#Employee Model

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=255,choices=(('Manager','Manager'),('Software Developer','Software Developer'),('Project Leader','PL')))    

    company = models.ForeignKey(Company, on_delete=models.CASCADE)