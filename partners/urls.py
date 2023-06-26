from django.conf import settings
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^partners/$', views.PartnersCatalogView, name='partners-catalog'),
    url(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/$', views.PartnerView, name='partner'),
    url(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/course/{}$'.format(settings.COURSE_ID_PATTERN), views.PartnerCourseView, name='partner-course'),
    url(r'^partners/(?P<partner_name>[a-zA-Z\d-]+)/expert/(?P<expert_id>\d+)$', views.ExpertView, name='expert'),
    url(r'^lakip/$', TemplateView.as_view(template_name="lakip-landing.html"), name='lakip'),
]

#  from django.conf import settings
# '{}'.format(settings.COURSE_ID_PATTERN)
# (?P<course_id>[^/+]+(/|\+)[^/+]+(/|\+)[^/?]+)
