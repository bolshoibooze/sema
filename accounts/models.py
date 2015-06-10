
import logging
import datetime
from django.db import models
from django.db.models import *
from django.conf import settings
from django.utils import timezone
from django.db.models.query import *
from django.contrib.auth.models import *
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.functional import cached_property
from django.utils.encoding import smart_unicode
from django.db.models import get_model

#signals
from django.dispatch import receiver
from django.db.models.signals import *

from sema.settings import *

from uuid import uuid4
def generateUUID():
    return str(uuid4())
    
"""    
def instantiate_notifications_wrapper(sender, **kwargs):
    from signal_hub.models import instantiate_notifications
    instantiate_notifications(sender, **kwargs) 
    
def instantiate_org_wrapper(sender, **kwargs):
    from signal_hub.models import instantiate_org
    instantiate_org(sender, **kwargs)
    
def instantiate_account_wrapper(sender, **kwargs):
    from signal_hub.models import instantiate_account
    instantiate_account(sender, **kwargs)
"""


class CustomUserManager(BaseUserManager):
    def create_user(self, id_number, password=None, **extra_fields):
        now = timezone.now()
        if not id_number:
            raise ValueError('The username must be set')
        #email = UserManager.normalize_email(email)
        user = self.model(id_number=id_number,
                          is_staff=False,is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, id_number, password, **extra_fields):
        u = self.create_user(id_number, password, **extra_fields)
        u.is_admin = True
        u.save(using=self._db)
        return u
                
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
       max_length=30, unique=True,
       verbose_name = 'Username'
    )
    full_name = models.CharField(
       max_length=50,null=True,blank=True,
       verbose_name='First & Last Name'
    )
    phone_number = models.CharField(
       max_length=15,
       verbose_name='Phone Number'
    )
    email = models.EmailField(
       max_length=255,null=True,
       blank=True
    )
    is_therapist = models.BooleanField(
       default=False
    )
    mug_shot = models.ImageField(
       upload_to='images/avatar',
       null=True,blank=True
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number',]
    objects = CustomUserManager()
    class Meta(object):
        db_table = 'CustomUser'
        verbose_name_plural = 'CustomUsers'
        
    def __unicode__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.full_name)
           
    def get_full_name(self):
        #the user is identified by their id_number
        return self.full_name
        
    def get_short_name(self):
        return self.full_name
        
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
                 
    def save(self,*args,**kwargs):
        super(CustomUser,self).save(*args,**kwargs)

"""       
models.signals.post_save.connect(instantiate_notifications_wrapper,sender=CustomUser) 
models.signals.post_save.connect(instantiate_org_wrapper,sender=CustomUser)
models.signals.post_save.connect(instantiate_account_wrapper,sender=CustomUser) 
"""
