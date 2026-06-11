from django.db import models


class Student(models.Model):


    FEE_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Partial', 'Partial'),
    ]
        
    name = models.CharField(max_length=100)
    aadhaar_card= models.CharField(max_length=12)
    father_name = models.CharField(max_length=20)
    whatsapp =models.CharField(max_length=10)
    address = models.TextField()
    joining_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_status = models.CharField(
        max_length=20,
        choices=FEE_STATUS_CHOICES,
        default= 'Pending'
    )
    fee_due_date = models.DateField(null=True, blank=True)

    last_payment_date = models.DateField(null=True, blank=True)
    
    receipt_url = models.URLField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
    
    

class Payment(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=17,
        decimal_places=2
    )

    payment_date = models.DateField(
        auto_now_add=True
    )

    receipt_url = models.CharField(
    max_length=500,
    blank=True,
    null=True
    )

    def __str__(self):
        return f"{self.student.name} - ₹{self.amount}"

class Settings(models.Model):

    library_name = models.CharField(max_length=200)
    library_address = models.TextField()

    contact_number = models.CharField(max_length=15)
    email = models.EmailField()

    opening_time = models.TimeField()
    closing_time = models.TimeField()

    cafe_name = models.CharField(max_length=200)

    gst_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    service_charge = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    email_notifications = models.BooleanField(
        default=True
    )

    whatsapp_notifications = models.BooleanField(
        default=True
    )

    dark_mode = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.library_name
    
    
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)

#     def __str__(self):
#         return self.name