from django.shortcuts import render,get_object_or_404
from .models import Partner,PartnerCourse,Advisor
from django.utils.text import slugify
from django.http import Http404

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

from datetime import date

import requests

# def PartnersView(request):
    #CoursesList = Course.objects.order_by('-rank')[:3]
    #context = {'landObjList':landObjList,'partnerObjList':partnerObjList}
    # return render(request, 'partners.html')

def PartnerView(request,partner_name):
    partner = get_object_or_404(Partner, slugName=partner_name)
    if not partner:
        raise Http404
    # courses = PartnerCourse.objects.filter(partner=partner)
    advisors = Advisor.objects.filter(partner=partner)
    courses = CourseOverview.get_all_courses(orgs=[partner.org])

    return render(request, 'partners.html', {'partner': partner,  'courses':courses, 'advisors':advisors, 'date_today':date.today})

# def CourseView(request,partner_name,course_name):
#     course = get_object_or_404(Course, slugTitle=course_name)
#     return render(request, 'partners.html', {'course': course})
#
# def AdvisorView(request,partner_name,advisor_id):
#     advisor = get_object_or_404(Advisor, pk=advisor_id)
#     return render(request, 'partners.html', {'advisor': advisor})
