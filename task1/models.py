from django.contrib.auth.hashers import make_password
from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    age = models.IntegerField()
    password = models.CharField(max_length=255, null=True)


    def save(self, *args, **kwargs):
        if self.pk is None:
            self.password = make_password(self.password)
        super(Buyer, self).save(*args, **kwargs)


class Game(models.Model):
    title = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyers = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "новости"
        ordering = ['-created_at']

