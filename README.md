# To Install:

1. Install with `pip install -e .` within this folder within the edx platform virtual environment.
2. Add "partners" to the "ADDL_INSTALLED_APPS" array in `lms.env.json` (you may have to create it if it doesn't exist.)
3. Run migrations.
4. Start/restart the LMS.


## Templates Directory
Add this to envs.common:

TEMPLATES_DIR = {
  ...
  OPENEDX_ROOT / 'features' / 'partners_pages' / 'partners' / 'templates',
}

## ADD TO LMS URLS
urlpatterns += [
    url(r'', include('partners.urls')),
]

# To Use:

## In creating Partner records
Make sure that both Partner and Organization records exist. They must have identical 'org' fields. Also, make sure the the 'org' name is also exactly the one used when the courses were created. This makes the rendering of associated course objects work.

## In creating PartnerCourse records
Make sure to use the exact course_id of the course. This means that the course must exist.

## Uploading logos, banners, profile pictures:
These are uploaded through the admin site when creating the records. The raw files are uploaded within the server (ec2 instance) at the directory path: /edx/var/edxapp/uploads/partners/

*For course images rendered on the course boxes and on the page banners, the course image set at the studio is used.
