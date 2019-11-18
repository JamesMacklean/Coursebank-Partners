from django.shortcuts import render,get_object_or_404
from .models import Partner, PartnerCourse, Expert
from django.utils.text import slugify
from django.http import Http404

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from opaque_keys.edx.keys import CourseKey

from datetime import date

import requests

def PartnersCatalogView(request):
    """ renders all partners in main partners page """
    link_partners = []
    for course in PartnerCourse.objects.all():
        if course.partner not in link_partners:
            link_partners.append(course.partner)
    partners = Partner.objects.filter(is_active=True).order_by('-ranking')
    context = {'partners': partners, 'link_partners': link_partners}
    return render(request, 'partners.html', context)

def PartnerView(request,partner_name):
    """ renders partner and corresponding experts and courses in its own partner page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    experts = Expert.objects.filter(is_active=True).filter(partner=partner)
    partner_courses = PartnerCourse.objects.filter(is_active=True).filter(partner=partner)
    courses = []
    for partner_course in partner_courses:
        course_key = CourseKey.from_string(partner_course.course_id)
        courseoverview = CourseOverview.get_from_id(course_key)
        courses.append(courseoverview)
    context = {'partner': partner,  'courses':courses, 'experts':experts}
    return render(request, 'partner.html', context)

def PartnerCourseView(request,partner_name,course_id):
    """ renders course in its own course page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    partner_course = get_object_or_404(PartnerCourse, course_id=course_id)
    course_key = CourseKey.from_string(course_id)
    course = CourseOverview.get_from_id(course_key)
    context = {'partner': partner, 'partner_course': partner_course, 'course': course}
    return render(request, 'partner_course.html', context)

def ExpertView(request,partner_name,expert_id):
    """ renders expert in its own expert page """
    partner = get_object_or_404(Partner, slugName=partner_name)
    expert = get_object_or_404(Expert, pk=expert_id)
    partner_courses = PartnerCourse.objects.filter(experts__id__exact=expert_id)
    courses = []
    for partner_course in partner_courses:
        course_key = CourseKey.from_string(partner_course.course_id)
        courseoverview = CourseOverview.get_from_id(course_key)
        courses.append({'courseoverview':courseoverview, 'partner_course':partner_course})
    context = {'partner': partner, 'expert': expert, 'courses': courses}
    return render(request, 'expert.html', context)

# get list of all existing course ids
# list_of_all_course_ids = CourseOverview.get_all_course_keys()
