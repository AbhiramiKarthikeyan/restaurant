from django.db import models

from django.contrib.auth.models import User


    # Create your models here.
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class customer_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100,null=True)

class restaurant_reg(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    oname=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    oaddress=models.CharField(max_length=100,null=True)
    license=models.ImageField(null=True)
    payment=models.CharField(max_length=100,null=True)


 
class add_photo(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(restaurant_reg,on_delete=models.CASCADE,null=True)
    image=models.ImageField(null=True)


class add_loc(models.Model):
    restaurant = models.ForeignKey(restaurant_reg,on_delete=models.CASCADE,null=True)
    location=models.CharField(max_length=100,null=True)
    lmap=models.CharField(max_length=1000,null=True)    
    otime=models.CharField(max_length=100,null=True)
    ctime=models.CharField(max_length=100,null=True)


class add_menu(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(restaurant_reg,on_delete=models.CASCADE,null=True)
    mname=models.CharField(max_length=100,null=True)
    image=models.ImageField(null=True)
    price=models.CharField(max_length=100,null=True)
    availability=models.CharField(max_length=100,null=True)




class customer_feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,null=True)
    feedback=models.CharField(max_length=1000,null=True)



class add_blogs(models.Model):
   
    bname=models.CharField(max_length=100,null=True)
    blog=models.CharField(max_length=1500,null=True)
    image=models.ImageField(null=True)
    





class add_specials(models.Model):
    restaurant = models.ForeignKey(restaurant_reg,on_delete=models.CASCADE,null=True)
    sstype=models.CharField(max_length=100,null=True)
    sname=models.CharField(max_length=100,null=True)
    price=models.CharField(max_length=100,null=True)
    sdes=models.CharField(max_length=1000,null=True)
    image=models.ImageField(null=True)

class restaurant_feedback(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100,null=True)
    feedback=models.CharField(max_length=1000,null=True)

class customer_reviews(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(restaurant_reg,on_delete=models.CASCADE,null=True)
    feedback=models.CharField(max_length=1000,null=True)
    name=models.CharField(max_length=100,null=True)











