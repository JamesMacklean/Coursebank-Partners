from django.shortcuts import render,get_object_or_404
from .models import Partner, PartnerCourse, Expert
from django.utils.text import slugify
from django.http import Http404

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

from datetime import date

import requests

def PartnersCatalogView(request):
    """ renders all partners in main partners page """
    partners = Partner.objects.all()
    context = {'partners': partners}
    return render(request, 'partners.html', context)

def PartnerView(request,partner_name):
    """ renders partner and corresponding experts and courses in its own partner page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    experts = Expert.objects.filter(partner=partner)
    courses = CourseOverview.get_all_courses(orgs=[partner.org])
    context = {'partner': partner,  'courses':courses, 'experts':experts}
    return render(request, 'partner.html', context)

def PartnerCourseView(request,partner_name,course_id):
    """ renders course in its own course page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    course = CourseOverview.get_from_id(course_id)
    context = {'partner': partner, 'course': course}
    return render(request, 'partner_course.html', context)

def ExpertView(request,partner_name,expert_id):
    """ renders expert in its own expert page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    expert = get_object_or_404(Expert, pk=expert_id)
    partner_courses = PartnerCourse.objects.filter(experts=expert)
    courses = []
    for partner_course in partner_courses:
        course = CourseOverview.objects.get(id=partner_course.course_id)
        courses.append(course)
    context = {'partner': partner, 'expert': expert, 'courses': courses}
    return render(request, 'expert.html', context)

# get list of all existing course ids
# list_of_all_course_ids = CourseOverview.get_all_course_keys()
