from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        
        if not email:
            raise ValueError('Desolé, veuillez saisir un email')
        
        email=self.normalize_email(email)
        user=self.model(email=email,username=username)
        
        user.set_password(password)
        
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True
        
        user.save(using=self._db)
        return user   

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, default='Anonymous', unique=True)
    email = models.EmailField(max_length=254, unique=True,blank=True,null=True)
    avatar=models.ImageField(upload_to='users_avatar',blank=True,null=True)
  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active=models.BooleanField(default=True,blank=True,null=True)
    is_staff=models.BooleanField(default=False,blank=True,null=True)

    # USERNAME_FIELD='email'
    # REQUIRED_FIELDS=['username']

    USERNAME_FIELD='username'
    # REQUIRED_FIELDS=['username']
    
    objects= UserProfileManager()
    
    class Meta:
        verbose_name="Profil"

    def __str__(self) -> str:
        return self.username