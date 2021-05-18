from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Worker(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Support(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
