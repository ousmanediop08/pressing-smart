from django import forms
from django.db import models

# Create your models here.

class Contact(models.Model):

    name = models.CharField(max_length=120)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email

class Subscribe(models.Model):

    PAYMENT_TYPE = (
        ('Cash','Cash'),
        ('Orange Money','Orange Money'),
        ('Wave','Wave'),
        )


    CHOICE_TYPE = (
            ('Complet','Complet'),
            ('Sec','Nettoyage à sec'),
    )

    name = models.CharField(max_length=120)
    adress = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=18, null=True)
    paiement = models.CharField(max_length=220, choices=PAYMENT_TYPE)
    choice = models.CharField(max_length=220, choices=CHOICE_TYPE,null=True)
    date_rv = models.DateTimeField(auto_now_add=False)
    #bank = models.CharField(max_length=220)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
# phone = models.PhoneNumberField(max_length=18, null=True)

