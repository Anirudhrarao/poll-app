from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Poll(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    questions = models.TextField()
    options_one = models.CharField(max_length=120)
    options_two = models.CharField(max_length=120)
    options_three = models.CharField(max_length=120)
    options_four = models.CharField(max_length=120)
    counting_for_opt_one = models.IntegerField(default=0)
    counting_for_opt_two = models.IntegerField(default=0)
    counting_for_opt_three = models.IntegerField(default=0)
    counting_for_opt_four = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username
