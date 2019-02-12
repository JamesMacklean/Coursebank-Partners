from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^partners', views.PartnersCatalogView, name='partners-catalog'),
    url(r'^partners/(?P<partner_name>[a-z\d-]+)/$', views.PartnerView, name='partner'),
    url(r'^partner/(?P<partner_name>[a-zA-Z\d-]+)/course/{}$'.format(settings.COURSE_ID_PATTERN), views.PartnerCourseView, name='partner-course'),
    url(r'^partner/(?P<partner_name>[a-zA-Z\d-]+)/expert/(?P<expert_id>\d+)$', views.ExpertView, name='expert'),
]

#  from django.conf import settings
# '{}'.format(settings.COURSE_ID_PATTERN)
# (?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)
