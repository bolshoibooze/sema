
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
