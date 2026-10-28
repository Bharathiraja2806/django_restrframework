from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# class register(models.Model):

#     name = models.CharField(max_length=30)
#     email = models.EmailField()
#     password = models.CharField(max_length=10)
#     confirm_password = models.CharField(max_length=10)

#     def __str__(self):
#         return self.name

# class login(models.Model):

#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=10)

#     def __str__(self):
#             return self.name 