from django.db import models
from django.utils.translation import gettext as _
from django.utils.timezone import now
# Create your models here.

class LinkedinPost(models.Model):
    company_name = models.CharField(_("Company Name"), max_length=50) 
    date_posted = models.CharField(_('Date Posted'),max_length=40)
    media_type = models.CharField(_('Media type'),max_length=40)
    post_data = models.TextField(_("Post Description"))
    likes = models.IntegerField(_("Total Likes of Post"))
    comments = models.IntegerField(_("Total Comments of Comment"))
    views = models.CharField(_('Post Views'),max_length=40)
    media_link = models.TextField(_('Media Links'))
    date_on_create = models.DateField(_("Date on Create"), default=now())

class CompanyList(models.Model):
    company_urls = models.CharField(_("Company Urls"), max_length=150)