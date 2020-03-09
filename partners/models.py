from django.db import models
from django.utils.text import slugify
from datetime import date

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class Partner(models.Model):
    org = models.CharField(
        max_length=255,
        help_text='organization short name ex. OrgX used when creating courses',
        unique=True)
    name = models.CharField(max_length=255,default='No name')
    slugName = models.SlugField(max_length=255,editable=False, default=slugify(name),unique=True)
    description = models.TextField(default='No description set.')
    logo = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for logo images. This logo will be used on partner pages.',
        null=True, blank=True, max_length=255)
    logo_url = models.URLField(max_length=500)
    banner = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for banner images. This banner will be used on partner pages.',
        null=True, blank=True, max_length=255)
    banner_url = models.URLField(max_length=500)
    is_active = models.BooleanField(default=True)
    ranking = models.PositiveSmallIntegerField(default=0)
    cert_desc = models.TextField(default="")

    class Meta:
        ordering = ['-ranking']

    def save(self, *args, **kwargs):
        self.slugName = slugify(self.name)
        super(Partner, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class PartnerCourse(models.Model):
    course_id = models.CharField(max_length=255,primary_key=True)
    partner = models.ForeignKey(
        'Partner',
        related_name='partner_course',
        help_text='partner/organization associated with this course',
        on_delete=models.CASCADE
        )
    experts = models.ManyToManyField(
        'Expert',
        related_name='partner_course',
        help_text='Experts that facilitate this course',
        blank=True)
    is_active = models.BooleanField(default=True)

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
    description = models.TextField(default='No description set.')
    position = models.CharField(max_length=30,default='Expert')
    profilePic = models.ImageField(
        upload_to='partners',
        help_text='Please add only .PNG files for profile images. This image will be used on partner pages.',
        null=True, blank=True, max_length=255)
    profile_pic_url = models.URLField(max_length=500)
    partner = models.ForeignKey(
        'Partner',
        related_name='expert',
        help_text='partner/organization associated with this expert',
        on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
