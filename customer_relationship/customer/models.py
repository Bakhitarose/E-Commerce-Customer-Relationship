from django.db import models
""" The relationship between customer and order models is a
    one-to-many relationship where each Customer can
      have multiple Orders."""

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=255) #string field for the first name.
    lastname = models.CharField(max_length=255) #String field for the last name.
    email = models.EmailField(unique=True) #Unique email to ensure none of the customers share the same email address
    phone_number = models.CharField(max_length=15, blank=True) #an OPTIONAL string field for the phone number.
    created_at = models.DateTimeField(auto_now_add=True) # A timestamp field that records when a customer was created.
    updated_at = models.DateTimeField(auto_now=True) # A timestamp field that records when the customer information is modified.

    def __str__(self): #Method that defines how an object is represented as a string.
        return f"{self.firstname} {self.lastname}"
    
""" A foreign key is created to in the order model to
    link it to the customer model"""

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders') #A foreign key that links an order to a specific customer(1 to many relationship).
    order_date = models.DateTimeField(auto_now_add=True) # A timestamp field that records when the order was placed.
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) #Decimal field that shows the total amount for an Order. 
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled','Cancelled'),
    ], default='pending') # Choice field that shows the current status of the order.