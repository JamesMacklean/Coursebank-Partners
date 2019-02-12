from django.db import models
from django.utils.text import slugify
from datetime import date

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class Partner(models.Model):
    org = models.TextField(max_length=255, help_text='organization short name ex. OrgX used when creating courses')
    name = models.CharField(max_length=75,default='No name',unique=True)
    slugName = models.SlugField(max_length=75,editable=False, default=slugify(name),unique=True)
    description = models.CharField(max_length=500,default='No description set.')
    logo = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for logo images. This logo will be used on partner pages.',
        null=True, blank=True, max_length=255
        )
    banner = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for banner images. This banner will be used on partner pages.',
        null=True, blank=True, max_length=255
        )
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slugName = slugify(self.name)
        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PartnerCourse(models.Model):
    course_id = models.CharField(max_length=255,primary_key=True)
    partner = models.ForeignKey(
        'Partner',
        on_delete=models.CASCADE
        )
    experts = models.ManyToManyField(
        'Expert'
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
        get_course = CourseOverview.objects.filter(id=self.course_id)
        if get_course is not None:
            return date.today() < get_course.start
        else:
            return None

    def __str__(self):
        return self.course_id

    # def save(self, *args, **kwargs):
    #     self.slugTitle = slugify(self.title)
    #     super(Course, self).save(*args, **kwargs)

class Expert(models.Model):
    name = models.CharField(max_length=75,default='No name')
    description = models.CharField(max_length=500,default='No description set.')
    position = models.CharField(max_length=30,default='Expert')
    profilePic = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for profile images. This image will be used on partner pages.',
        null=True, blank=True, max_length=255
        )
    partner = models.ForeignKey(
        'Partner',
        on_delete=models.CASCADE,
        default=-1
    )

    def __str__(self):
        return self.name
