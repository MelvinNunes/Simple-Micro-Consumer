from django.db import models

# Create your models here.

class Province(models.Model):
    province_name = models.CharField(max_length=255, null=False)