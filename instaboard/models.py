from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

class Account(models.Model):
  user = models.ManyToManyField(User, help_text="Select a user for this book")
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  full_name = models.CharField(max_length=255, null=True, blank=True)
  profile_pic_url = models.CharField(max_length=255, null=True, blank=True)
  profile_pic_id = models.CharField(max_length=255, null=True, blank=True)
  phone_number = models.CharField(max_length=255, null=True, blank=True)
  slug = models.SlugField(max_length=60, blank=True)

  def __str__(self):
    return self.username

  def save(self, *args, **kwargs):
    if not self.id:
        print(self.id)
        self.slug = slugify("%s" % (self.username)) 
    super(Account, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('detail', args=[str(self.slug)])