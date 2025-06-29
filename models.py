from django.db import models

# Create your models here.
class Drinks(models.Model):
    tea=models.TextField(max_length=50)
    coffee=models.CharField(max_length=50)
    snacks=models.CharField(max_length=50)
    juice=models.TextField(max_length=50)

    class Meta:
        db_table="drinks"



class employee(models.Model):
    name=models.TextField(max_length=50)
    emp_code=models.TextField(max_length=20)
    position=models.CharField(max_length=50)


#this for product table

class product(models.Model):
    pname=models.CharField(max_length=25)
    pprice=models.BigIntegerField()
    prating=models.TextField(max_length=15)


class customer(models.Model):
    cname=models.CharField(max_length=20)
    number=models.BigIntegerField()
    mail=models.TextField(max_length=20)
    
class order(models.Model):
    csname=models.CharField(max_length=30)
    product=models.CharField(max_length=30)
    price=models.TextField(max_length=30)
    add=models.CharField(max_length=25)





class courses(models.Model):
    crname=models.CharField(max_length=30)
    price=models.CharField(max_length=20)
    duration=models.BigIntegerField()
    doj=models.DateTimeField(auto_now=True)

class photo(models.Model):
    name=models.TextField(max_length=30)
    img=models.ImageField(upload_to='pic')
