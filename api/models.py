from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='images/') 


class endpoint(models.Model):
    title = models.CharField(max_length=100)
    dicription = models.TextField()
    image = models.ImageField(upload_to='uploads/') 




    
