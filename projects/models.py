from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    image = models.FilePathField(path="", default='/tba.png')
