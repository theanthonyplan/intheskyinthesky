from django.db import models

# Create your models here.
class Record(models.Model):
    summary = models.TextField(max_length=2000)
    is_human = models.BooleanField()
    correct_count = models.IntegerField(default=0)
    incorrect_count = models.IntegerField(default=0)

    def __str__(self):
        return self.summary[:100]
