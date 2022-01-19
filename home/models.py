from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    desc=models.TextField(max_length=100)
    date=models.DateField(default='02-02-2021')
    def __str__(self):
        return self.name

class Order(models.Model):
    Your_Name=models.CharField(max_length=40)
    Phone_Number=models.IntegerField()
    Table_Number=models.IntegerField()
    Item_name=models.CharField(max_length=30)
    Total_Item=models.IntegerField()
    Address=models.TextField(null=True, blank=True)
    #time=models.DateField(default='02-02-2021')
    
    def __str__(self) :
        return self.Item_name
    