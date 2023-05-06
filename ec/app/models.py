from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES=(
    ('CR','american food'),
    ('ML','Moroccan food'),
    ('LS','Turkish food'),
    ('MS','Greek food'),
    ('PN','Spanish food'),
    ('GH','Japanese food'),
)
STATE_CHOICES=(
    ('Tanger','Tanger'),
    ('Tétouan','Tétouan'),
    ('Chefchaouen','Chefchaouen'),
    ('Fnideq','Fnideq'),
    ('Oujda','Oujda'),
    ('Nador','Nador'),
    ('Berkane','Berkane'),
    ('Ifrane','Ifrane'),
    ('Azrou','Azrou'),
    ('Rabat','Rabat'),
    ('Temara','Temara'),
    ('Azilal','Azilal'),
    ('Casablanca','Casablanca'),
    ('Settat','Settat'),
    ('Mohammedia','Mohammedia'),
    ('Bouskoura','Bouskoura'),
    ('Marrakech','Marrakech'),
)



class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices= CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
    ('Pending', 'Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

