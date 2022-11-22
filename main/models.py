from django.db import models
from django.template.defaultfilters import slugify
import uuid
from phonenumber_field.modelfields import PhoneNumberField
from django_quill.fields import QuillField
from django.urls import reverse
from django.utils import timezone
from app_auth.models import *
from  embed_video.fields  import  EmbedVideoField

# Create your models here.
# la class de base 
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')

    class Meta:
        abstract=True
