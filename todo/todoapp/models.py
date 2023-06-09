from django.db import models

# Create your models here.
class Todo(models.Model):
    activity = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.activity
    