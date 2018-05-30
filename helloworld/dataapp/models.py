from django.db import models

# Create your models here.

class  Blog(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    Description = models.TextField(default='', blank=True)


    def __str__(self):
        return '%s' % self.title

    def __repr__(self):
        return "BlogPost('{}', '{}')".format(self.title, self.Description)

