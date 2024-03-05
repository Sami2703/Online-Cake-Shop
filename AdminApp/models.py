from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=20)

    def __str__(self):
        return self.cname

    class Meta:
        db_table = 'Category'

class Cake(models.Model):
    cakename = models.CharField(max_length=20)
    price = models.FloatField(default=200)
    description = models.CharField(max_length = 200)
    image = models.ImageField(default = 'abc.jpg',upload_to='Images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta:
        db_table = "Cake"


class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'UserInfo'

class MyCart(models.Model):
    cake = models.ForeignKey(Cake,on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"

class Accounts(models.Model):
    cardNo = models.CharField(max_length = 4)
    cvv = models.CharField(max_length =4)
    expiry = models.CharField(max_length = 8)
    balance = models.FloatField(default = 10000)

    class Meta:
        db_table = "Accounts"

class OrderMaster(models.Model):
    user = models.ForeignKey(UserInfo,on_delete = models.CASCADE)
    cake_details = models.CharField(max_length=200)
    total_amount = models.FloatField(default=1000)
    date_of_order = models.DateField()

    class Meta:
        db_table = "OrderMaster"
