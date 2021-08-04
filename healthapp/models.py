from django.db import models
import uuid
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from .managers import CounsellorUser
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

  #Fields that tie to the roles
  ADMIN = 1
  MANAGER = 2
  CLIENT = 3

  ROLE_CHOICES = (
    (ADMIN, 'Admin'),
    (MANAGER, 'Manager'),
    (CLIENT, 'Client')
  )
  class Meta:
    verbose_name = 'user'
    verbose_name_plural= 'users'
  uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length= 30, blank=True)
  last_name = models.CharField(max_length=50, blank=True)
  role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)



  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CounsellorUser()
  
  def __str__(self):
      return self.email

