from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_column='id')
    first_name = models.CharField(max_length=200, db_column='first_name')
    last_name = models.CharField(max_length=200, db_column='last_name')
    username = models.CharField(max_length=200, db_column='username')
    email = models.EmailField(max_length=200, null=False, db_column='email')
    otp = models.CharField(max_length=200, null=True, db_column='otp')
    password = models.CharField(max_length=200, null=False, db_column='password')
    phone_number = models.CharField(max_length=200, null=False, db_column='phone_number')
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True, db_column='profile_pic')
    two_factor_auth = models.BooleanField(default=False, db_column='two_factor_auth')
    location = models.CharField(max_length=200, null=True, db_column='location')
    refresh_token = models.CharField(max_length=200, null=True, db_column='refresh_token')
    is_verified = models.BooleanField(default=False, db_column='is_verified')
    created_at = models.DateTimeField(default=timezone.now, db_column='created_at')
    updated_at = models.DateTimeField(default=timezone.now, db_column='updated_at')
    user_type = models.CharField(max_length=200, null=True, db_column='user_type')

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = 'user'
        verbose_name_plural = 'users'
        ordering = ['-created_at']


