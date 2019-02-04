from django.db import models
from django.utils.text import slugify
from datetime import date

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class Partner(models.Model):
    name = models.CharField(max_length=75,default='No name',unique=True)
    slugName = models.SlugField(max_length=75,editable=False, default=slugify(name),unique=True)
    description = models.CharField(max_length=500,default='No description set.')
    logo = models.ImageField(
        upload_to='partners',
        help_text=_('Please add only .PNG files for logo images. This logo will be used on partner pages.'),
        null=True, blank=True, max_length=255
        )
    banner = models.ImageField(
        upload_to='partners',
        help_text=_('Please add only .PNG files for banner images. This banner will be used on partner pages.'),
        null=True, blank=True, max_length=255
        )
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slugName = slugify(self.name)
        super(Partner, self).save(*args, **kwargs)

class PartnerCourse(models.Model):
    course = models.ForeignKey(
        CourseOverview,
        on_delete=models.CASCADE
    )
    partner = models.ForeignKey(
    'Partner',
    on_delete=models.CASCADE,
    null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    # title = models.CharField(max_length=75,default='Course title',unique=True)
    # slugTitle = models.SlugField(max_length=75,editable=False, default=slugify(title),unique=True)
    # date_starting = models.DateField()
    # image = models.CharField(max_length=200)
    #
    # advisor = models.CharField(max_length=75)
    # canEarnCpd = models.BooleanField(default=False)
    # courseExpertNum = models.PositiveSmallIntegerField()
    # description = models.CharField(max_length=500)
    # linkToAuthor = models.CharField(max_length=75)
    # created_at = models.DateField(auto_now_add=True)
    # rank = models.PositiveSmallIntegerField()

    @property
    def is_starting(self):
        return date.today() < self.course.start

    # def save(self, *args, **kwargs):
    #     self.slugTitle = slugify(self.title)
    #     super(Course, self).save(*args, **kwargs)

class Advisor(models.Model):
    name = models.CharField(max_length=75,default='No name')
    description = models.CharField(max_length=500,default='No description set.')
    position = models.CharField(max_length=30,default='Advisor')
    profilePic = models.CharField(max_length=25)
    partner = models.ForeignKey(
        'Partner',
        on_delete=models.CASCADE,
        default=-1
    )
