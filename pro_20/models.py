from django.db import models

# Create your models here.


class customer(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Email = models.EmailField()
    User_Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.First_Name


class products(models.Model):
    Product_Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Quantity = models.IntegerField()
    Photo = models.FileField()

    def __str__(self):
        return self.Product_Name


class booking(models.Model):
    Product_Id = models.IntegerField()
    User_id = models.CharField(max_length=100)
    Product_Name = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Total = models.IntegerField()
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.Product_Id


class Wishlist(models.Model):
    User_id = models.CharField(max_length=100)
    Product_Id = models.IntegerField()
    Status = models.CharField(max_length=100)

    def __str__(self):
        return self.User_id


class Reviews(models.Model):
    User_id = models.CharField(max_length=100)
    Product_Id = models.IntegerField()
    Review = models.CharField(max_length=100)

    def __str__(self):
        return self.User_id



class Payments(models.Model):
    customer_id=models.CharField(max_length=100)
    booking_id=models.IntegerField()
    total_amount=models.IntegerField()
    status=models.CharField(max_length=100)

    def __str__(self):
        return self.booking_id

