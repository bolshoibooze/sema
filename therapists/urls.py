from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
#from django.conf.urls.defaults import *


from .views import *
from .models import *



urlpatterns = patterns('.views',
   #url(r'^withdrawals/$',WithdrawalFormView.as_view(),
        #name = 'withdrawals'),
        
        
        
)

