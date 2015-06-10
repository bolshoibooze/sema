import math
import datetime
from celery import Celery
from celery import shared_task
from django.conf import settings
from celery.utils.log import get_task_logger
from django.utils.translation import ugettext as _
from django.db.models.query import QuerySet
from socket import error as socket_error
from django.core import urlresolvers
from celery.contrib.methods import *
from django.utils import timezone
from django.db.models import *
from django.db import *





logger = get_task_logger(__name__)

