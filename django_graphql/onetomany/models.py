from django.db import models


# Create your models here.
class ModelOne(models.Model):
    description = models.CharField(max_length=120)

    def __str__(self):
        return self.description


class ModelTwo(models.Model):
    description = models.CharField(max_length=120)
    model_one = models.ForeignKey(ModelOne, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} - ModelOne {self.model_one}'
