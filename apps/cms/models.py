from django.db.models import *
from basic.models import Content


class ContentBlock(Content):
    """
    """
    class Meta:
        ordering = ['position', ]


# signals are separated to signals.py
# just for the sake of organization
import signals