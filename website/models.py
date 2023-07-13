from django.db import models


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    customer = models.CharField(max_length=50)
    notes = models.CharField(max_length=500)

    def __str__(self):
        return(f"{self.first_name} {self.last_name} {self.area} {self.customer} {self.notes}")