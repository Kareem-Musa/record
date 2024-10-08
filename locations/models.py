from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# state model
class State(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'الولايات'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('locations:state_list')

# hquarter model
class Hquarter(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=(''), related_name='state_hquarters', on_delete=models.CASCADE)
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
        return reverse('locations:hquarter_list')

# locality model
class Locality(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=_(''), related_name='state_localities', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'المحليات'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('locations:locality_list')

# unity model
class Unity(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=_(''), related_name='state_unities', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name=_(''), related_name='locality_unities', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'الوحدات الأدارية'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('locations:unity_list')

# city model
class City(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=50, unique=True)
    state = models.ForeignKey(State, verbose_name=_(''), related_name='state_cities', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name=_(''), related_name='locality_cities', on_delete=models.CASCADE)
    unity = models.ForeignKey(Unity, verbose_name=_(''), related_name='unity_cities', on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'المدن'

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(**kwargs)

    def get_absolute_url(self):
        return reverse('locations:city_list')
