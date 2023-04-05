from django.db import models

# Create your models here.
class one(models.Model):
    Onee=models.CharField(max_length=20,primary_key=True)
    tw=models.CharField(max_length=100)

    def __str__(self):
        return self.Onee


class two(models.Model):
    Onee=models.ForeignKey(one,on_delete=models.CASCADE)
    gg=models.CharField(max_length=100)

    def __str__(self):
        return self.Onee