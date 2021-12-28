from django.db import models
from django.contrib.auth.models import User


class Text(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    send_to = models.ManyToManyField(User, null=True)
    

    def __str__(self) -> str:
        return self.title