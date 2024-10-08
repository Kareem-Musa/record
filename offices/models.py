from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from locations.models import State

# hquarter model
class Hquarter(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=_(''), related_name='state', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'الرئاسات'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('offices:hquarter_list')

# sector model
class Sector(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=_(''), related_name='state_sectors', on_delete=models.CASCADE)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_(''), related_name='hquarter_sectors', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'القطاعات'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('offices:sector_list')

# office model
class Office(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=_(''), related_name='state_offices', on_delete=models.CASCADE)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_(''), related_name='hquarter_offices', on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, verbose_name=_(''), related_name='sector_offices', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'المكاتب'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('offices:office_list')
