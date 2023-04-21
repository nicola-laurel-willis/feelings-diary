from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    def __str__(self):
        return self.name
      
      
class DiaryEntry(models.Model):
    text = models.CharField(max_length=80)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return f"{self.text}, {self.pub_date}"