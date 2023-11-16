from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime


class Campus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    location = models.CharField(max_length=255)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)
    two_factor_auth = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    is_verified = models.BooleanField()
    user_type = models.CharField(max_length=255)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    created_at = models.DateTimeField()

class UserProperties(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

class PropertieInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_property = models.ForeignKey(UserProperties, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    longitude = models.IntegerField()
    latitude = models.IntegerField()
    short_description = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    house_type = models.CharField(max_length=255)
    created_at = datetime.now()

class HousePictures(models.Model):
    id = models.AutoField(primary_key=True)
    info = models.ForeignKey(PropertieInfo, on_delete=models.CASCADE)
    picture_url = models.CharField(max_length=255)
    posted = datetime.now()

class HouseVideos(models.Model):
    id = models.AutoField(primary_key=True)
    info = models.ForeignKey(PropertieInfo, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255)
    posted_date = datetime.now()

class Package(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    payment_date = datetime.now()
    amount = models.IntegerField()
    status = models.BooleanField()

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(PropertieInfo, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    liked_at = datetime.now()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(PropertieInfo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = datetime.now()

class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = datetime.now()
