from django import template
from django.conf import settings
from uuid import uuid1
register = template.Library()

@register.simple_tag(name='cache_bust')
def cache_bust():
    if settings.DEBUG:
        version = uuid1()
    else:
        version = os.environ.get('PROJECT_VERSION')
        if version is None:
            version = '1'
    return '__v__={version}'.format(version=version)