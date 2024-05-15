from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField()
    rubrics = models.JSONField()