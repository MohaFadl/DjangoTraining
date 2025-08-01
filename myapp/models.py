from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)


class Address(models.Model):
    client = models.ForeignKey(Client, related_name='addresses', on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10, blank=True, null=True)


class Lawyer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=255)


class Case(models.Model):
    STATUS_OPEN = 'O'
    STATUS_CLOSED = 'C'

    STATUS_CHOICES = [
        (STATUS_OPEN, 'Open'),
        (STATUS_CLOSED, 'Closed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client, related_name='cases', on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, related_name='cases', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_OPEN)
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['title' , 'lawyer' , 'status'])
        ]


class Appointment(models.Model):
    client = models.ForeignKey(Client, related_name='appointments', on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, related_name='appointments', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    purpose = models.TextField()



class Document(models.Model):
    case = models.ForeignKey(Case, related_name='documents', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='case_documents/')



class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount_percent = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])


class Invoice(models.Model):
    case = models.OneToOneField(Case, on_delete=models.CASCADE, related_name='invoice')
    issued_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    promotions = models.ManyToManyField(Promotion, blank=True, related_name='invoices')
