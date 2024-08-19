from django.db import models

# Create your models here.
#News model

class News(models.Model):
    
    headline=models.CharField(max_length=200)
    body=models.TextField()
    date=models.DateTimeField()
    
    
        
    def __str__(self):
        
        return self.headline
    
    