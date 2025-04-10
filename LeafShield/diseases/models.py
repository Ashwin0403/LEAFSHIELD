from django.db import models

class Predict(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    prevention = models.TextField()
    treatment = models.TextField()


    class Meta:
        db_table = 'predict'  # This explicitly sets the table name to 'predict'

   
    def __str__(self):
        return self.name
