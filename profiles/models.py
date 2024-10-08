from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.text import gettext_lazy as _
from locations.models import State, Hquarter, Locality, Unity


class Profile(models.Model):
    class ProfileType(models.TextChoices):
        MANAGER = 'MG', _('Manager')
        FINAN = 'FI', _('Finan')
        AUDITOR = 'AUD', _('Auditor')
        RESEARCHER = 'RES', _('Researcher')
    user = models.OneToOneField(User, verbose_name=_('المستخدم'), on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(verbose_name=_('الصورة'), blank=True, null=True, upload_to='images/')
    state = models.ForeignKey(State, verbose_name=_('الولاية'),
                                related_name='state_profiles', on_delete=models.CASCADE, blank=True, null=True)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_('الأمانة'),
                                related_name='hquarter_profiles', on_delete=models.CASCADE, blank=True, null=True)
    locality = models.ForeignKey(Locality, verbose_name=_('المحلية'),
                                related_name='locality_profiles', on_delete=models.CASCADE, blank=True, null=True)
    unity = models.ForeignKey(Unity, verbose_name=_('الوحدة الإدارية'),
                                related_name='unity_profiles', on_delete=models.CASCADE, blank=True, null=True)
    profile_type = models.CharField(verbose_name=_('الصلاحية'), max_length=3, choices=ProfileType.choices, null=True, blank=True)
    bio = models.TextField(verbose_name='معلومات إضافية', null=True, blank=True)
    active = models.BooleanField(default=True, blank=True, null=True)
    slug = models.SlugField(editable=False, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Profiles'


    def __str__(self):
        return self.user.username


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('employees:document_list')
