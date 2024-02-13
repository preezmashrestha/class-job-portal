from django.db.models import Model,CharField,IntegerField,DateField,ForeignKey,CASCADE,OneToOneField

#from .models import Customer




choice = {
        "DONE": "done",
        "PENDING": "pending",
       
       
    }
    

# Create your models here.

class Admin(Model):
     adminname=CharField(max_length=40)
     password=CharField(max_length=8)
     def __str__(self):
        return self.adminname 



class Orders(Model):
    nameofdealer=CharField(max_length=40)
    contactperson=CharField(max_length=40)
    nameofparticular=CharField(max_length=20)
    address=CharField(max_length=40)
    qty=IntegerField()
    total=IntegerField()
    phoneno=IntegerField()
    date=DateField(max_length=40)
    status=CharField(max_length=20,
        choices=choice,
        default="DONE",)
   
   

    def __str__(self):
        return self.nameofdealer
       

class Items(Model):
     item_name=CharField(max_length=40)
     instockqty=IntegerField()
     costprice=IntegerField()
     


     def __str__(self):
        return self.item_name
     

class OrderItem(Model):
     order_qty_price=ForeignKey(Orders, on_delete=CASCADE,default=None)
     item_qty_price =ForeignKey(Items, on_delete=CASCADE,default=None)
     
     item_name=CharField(max_length=40)
     profit=IntegerField()
     totalsoldout=IntegerField()


     def __str__(self):
        return self.item_name

        



class Customer(Model):
     cname=CharField(max_length=40)
     email=CharField(max_length=20)
     phoneno=IntegerField()

     def __str__(self):
        return self.cname

class Problems(Model):
     customerdetail=OneToOneField(Customer, on_delete=CASCADE,default=None)
     nameofproduct=CharField(max_length=40)
     buyedfromdealer=IntegerField()
     dateofpurchased=DateField(max_length=40)
     problemdetail=CharField(max_length=100)



     def __str__(self):
        return self.nameofproduct









#[python manage.py makemigrations] git add . git commit - git push origin python manage.py shell f/rom users.models import Job/ from django.utils import timezone/ a=job