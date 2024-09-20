from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


#Movie model
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to='movie/images/')
    url=models.URLField()

    #String representation of the text field     
    def __str__(self):
        
        return self.title




#Review mode
class Review(models.Model):
    text=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)    
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain=models.BooleanField()

    #String representation of the text field    
    def __str__(self):        
        return self.text
    
    
    
