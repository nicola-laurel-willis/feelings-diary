from django.db import models
      
class DiaryEntry(models.Model):
    entry_text = models.CharField(max_length=80)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return f"{self.entry_text}, {self.pub_date}"