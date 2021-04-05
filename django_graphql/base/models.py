from django.db import models


class SimpleSingle(models.Model):
    string_field = models.CharField(max_length=120)
    bool_field = models.BooleanField()
    float_field = models.FloatField()
    int_field = models.IntegerField()

    def __str__(self):
        return f'{self.string_field}  {self.bool_field} {self.float_field} {self.int_field}'

