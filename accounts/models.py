from django.db import models

# Create your models here.
class CUNEUser(models.Model):
    email = models.EmailField(max_length=255)
   
    @property
    def first_name(self):
        return self.email.split(".")[0]
        

    def __str__(self):
        return self.first_name