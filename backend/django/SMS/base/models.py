# ----- 3rd Party Libraries -----
import time
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    email = models.EmailField(max_length=1000, blank=False)
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + self.subject