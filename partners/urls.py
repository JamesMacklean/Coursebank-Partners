
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^catalog', views.PartnersView, name='catalog'),
    url(r'^(?P<partner_name>[a-z\d-]+)/$', views.PartnerView, name='partner'),
    # url(r'^(?P<partner_name>[a-z\d-]+)/course/(?P<course_name>[a-z\d-]+)$', views.CourseView, name='partner-course'),
    # url(r'^(?P<partner_name>[a-zA-Z\d-]+)\/advisor\/(?P<advisor_id>\d+)$', views.AdvisorView, name='advisor'),
]
