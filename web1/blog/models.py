from django.db import models

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Need = models.CharField(max_length=100)
    Offering = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)




    def __str__(self):
        return self.name
