from django.shortcuts import *
from django.utils import simplejson
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse,resolve
from django.template import RequestContext
from django.contrib.auth.models import *
from django.contrib import messages

from .forms import *
from .models import *
from accounts.models import *
from sema.settings import *
from ua_detector.views import *
from ua_detector.preview import *
from ua_detector.model_views import *
from ua_detector.generic_views import *
from django.contrib.auth import get_user
from django.views.decorators.cache import *
