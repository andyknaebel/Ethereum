from django.db import models

class employee(models.Model):
    First = models.CharField(max_length=50, default='', null=True)
    Last = models.CharField(max_length=50, default='', null=True)


    def __str__(self):
        return self.name

