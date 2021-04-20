from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)

    # def __str__(self):
    #     return '{}{}'.format(self.title + self.body)