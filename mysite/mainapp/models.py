from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class User_details(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Category(models.Model):
    name = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Finacne(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category)

    def __str__(self):
        return self.title
