from django.db import models

# Create your models here.
STATE_CHOICE = ((
    ("Bihar" , 'Bihar'),
    ("Madhya Pradesh" , 'Madhya Pradesh'),
    ("Rajasthan" , 'Rajasthan')
 ))

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE,max_length=50)
    gender = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images",blank=True)
    docs = models.FileField(upload_to="documents",blank=True)