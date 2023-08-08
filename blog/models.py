from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.PROTECT)
    # content_type = models.CharField(max_length=50)

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=10000)
    user = models.ForeignKey(User, default=None, on_delete=models.PROTECT)
    # date_time = models.DateTimeField()