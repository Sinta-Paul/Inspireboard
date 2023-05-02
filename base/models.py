from django.db import models
from django.contrib.auth.models import User

    
class MoodBoard(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=300,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    mood_board = models.ForeignKey(MoodBoard, on_delete=models.CASCADE, related_name='images')


