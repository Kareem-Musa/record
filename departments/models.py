from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from locations.models import State, Locality, Unity
from employees.models import Dgree
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Planning(models.Model):
    name = models.CharField(verbose_name=_('الإدارة التخطيطية'), max_length=30, unique=True)
    state = models.ForeignKey(State, verbose_name=_('الأمانة'), related_name='state_plannings', on_delete=models.CASCADE)
    top_management = models.ForeignKey('self', verbose_name=_('الأدارة العليا'), related_name='planning_plannings',
                                            on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('الإدارات التخطيطية')
        ordering = ['created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('departments:planning_list')

# Management
class Management(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=30, unique=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('الإدارات')
        ordering = ['created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('departments:planning_list')

class Department(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=30, unique=True)
    management = models.ForeignKey('self', verbose_name=_(''), related_name='department_related', on_delete=models.CASCADE ,null=True, blank=True)
    min_dgree = models.ForeignKey(Dgree, verbose_name=_(''), related_name='dgree_departmants', on_delete=models.CASCADE)
    # state = models.ForeignKey(State, verbose_name=_('الولاية'), related_name='state_departments', on_delete=models.CASCADE, null=True, blank=True)
    # locality = models.ForeignKey(Locality, verbose_name=_('المحلية'), related_name='locality_departments', on_delete=models.CASCADE, null=True, blank=True)
    # unity = models.ForeignKey(Unity, verbose_name=_('الوحدة الإدارية'), related_name='unity_departments', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = _('الإدارات')
        ordering = ['created']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('departments:department_list')
