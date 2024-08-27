from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Unique related_name for CustomUser
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',  # Unique related_name for CustomUser
        blank=True,
    )
    
class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='otps',null=True)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        return not self.is_verified and (timezone.now() - self.created_at).total_seconds() < 300  # OTP valid for 5 minutes

class ProjectUser(AbstractUser):
    """Model to store extra details of user"""

    dob = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(
        max_length=100, null=True, blank=True, default='')
    age = models.IntegerField(null=True, blank=True)
    languages = models.CharField(
        max_length=100, null=True, blank=True, default='')
    image = models.ImageField(
        upload_to='profile_pictures/',
        null=True, default=None, blank=True)
    hobbies = models.CharField(
        max_length=100, null=True, blank=True, default='')
    phone = models.CharField(
        max_length=100, null=True, blank=True, default='')
    address = models.TextField(
        max_length=100, null=True, blank=True, default='')
    pincode = models.CharField(
        max_length=20, default='', null=True, blank=True)
    is_registered = models.BooleanField(null=True, blank=True, default=False)
    is_employ = models.BooleanField(null=True, blank=True)
    is_short_term = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.first_name
