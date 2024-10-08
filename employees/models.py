from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from locations.models import State, Locality, Unity, City
from offices.models import Hquarter, Sector, Office

# Range model
class Range(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=20, unique=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'القطاعات'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('employees:range_list')

# Bonus model
class Bonus(models.Model):
    name = models.CharField(verbose_name=_(''), max_length=20, unique=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'العلاوات'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('employees:bonus_list')

# Dgree model
class Dgree(models.Model):
    class Bonuses(models.TextChoices):
        FIRST = '1', '1'
        SECOND = '2', '2'
        THIRD = '3', '3'
        FOURTH = '4', '4'
        FIFTH = '5', '5'
        SIXTH = '6', '6'
        SEVENTH = '7', '7'
        EIEGTHTH = '8', '8'
        NINETH = '9', '9'
    class EmployeeType(models.TextChoices):
        EM = 'emp', 'موظف'
        WK = 'wk', 'عامل'

    name = models.CharField(verbose_name=_('الدرجة'), max_length=50, unique=True)
    tag = models.CharField(verbose_name=_('التعريف'), max_length=100, null=True, blank=True)
    base_salary = models.FloatField(verbose_name=_('المرتب الاساسى'))
    bonus = models.CharField(verbose_name=_('العلاوة'), max_length=2, choices=Bonuses.choices)
    section = models.CharField(verbose_name=_('القطاع'), max_length=20)
    begin_date = models.DateField(verbose_name=_('التاريخ'), null=True, blank=True)
    monthly_add = models.FloatField(verbose_name=_('المنحة الشهرية'), null=True, blank=True)
    yearly_add = models.FloatField(verbose_name=_('المنحة السنوية'), null=True, blank=True)
    emp_type = models.CharField(verbose_name=_('نوع الوظيفة'), max_length=3, choices=EmployeeType.choices)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'الدرجات'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('employees:dgree_list')

# Maritial Status
class MRITIAL_STATUS(models.TextChoices):
    MARRIED = 'MR', 'Married'
    SINGLE = 'SN', 'Single'
    DIVORCED = 'DV', 'Divorced'
    WIDOW = 'WD', 'Widow'

class QUALIFICATIONS(models.TextChoices):
    PROFESSOR = 'PR', 'بروفيسور'
    DECTORATE = 'DR', 'دكتوراة'
    MASTER = 'MS', 'ماجستير'
    BACHLOR = 'BS', 'بكلاريوس'
    DIPLOMA = 'DP', 'دبلوم'
    SECONDARY = 'ثانوى'
    WC = 'WC', 'دون شهادة'

class EMPLOYEE_TYPE(models.TextChoices):
    EMPLOYEE = 'EM', 'موظف'
    WORKER = 'WK', 'عامل'

# Employee model
class Employee(models.Model):
    idn = models.IntegerField(verbose_name=_('الرقم الوظيفى'), unique=True)
    name = models.CharField(verbose_name=_('الأسم'), max_length=50)
    national_no = models.IntegerField(verbose_name=_('الرقم الوطنى'), unique=True)
    birth_date = models.DateField(verbose_name=_('تاريخ الميلاد'))
    image = models.FileField(verbose_name=_('الصورة'), upload_to='images/', null=True, blank=True)
    state = models.ForeignKey(State, verbose_name=_('الولاية'), related_name='state_employees', on_delete=models.CASCADE)
    locality = models.ForeignKey(Locality, verbose_name=_('المحلية'), related_name='locality_employees', on_delete=models.CASCADE)
    unity = models.ForeignKey(Unity, verbose_name=_('الوحدة الأدارية'), related_name='unity_employees', on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name=_('المدينة'), related_name='city_employees', on_delete=models.CASCADE)
    address = models.CharField(verbose_name=_('العنوان'), max_length=100, null=True, blank=True)
    hquarter = models.ForeignKey(Hquarter, verbose_name=_('الولاية الحالية'), related_name='hquarter_emps', on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, verbose_name=_('القطاع'),
                                        related_name='sector_emps', on_delete=models.CASCADE, null=True, blank=True)
    office = models.ForeignKey(Office, verbose_name=_('المكتب'), related_name='office_emps',
                                        on_delete=models.CASCADE, null=True, blank=True)
    dgree = models.ForeignKey(Dgree, verbose_name=_('الدرجة الوظيفية'), related_name='dgree_employees', on_delete=models.CASCADE)
    # new
    documents = models.ImageField(verbose_name=_(''), null=True, blank=True, upload_to='images/')
    maritial_status = models.CharField(verbose_name=('الحالة الإجتماعية'), max_length=2, choices=MRITIAL_STATUS.choices)
    wives_no = models.IntegerField(verbose_name=_('عدد الزوجات'))
    sons_no = models.IntegerField(verbose_name=_('عدد الإبناء'))
    education = models.CharField(verbose_name=_('المستوى التعليمى'), max_length=5, choices=QUALIFICATIONS.choices)
    employee_type = models.CharField(verbose_name=_('نوع الوظيفة'), max_length=5, choices=EMPLOYEE_TYPE.choices)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'القوى العاملة'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('employees:dgree_list')

class DocumentTags(models.TextChoices):
    MARRIAGE_LIENCENCE = 'ML', 'قسيمة زواج'
    BIRTH_DATE = 'BD', 'شهادة ميلاد'
    CHILD_BIRTH = 'CB', 'عقيقة'
    QUALIFICATION = 'QL', 'مؤهل'
    IDENTITY = 'ID', 'ورقة ثبوتية'


class Document(models.Model):
    code = models.CharField(verbose_name=_(''), max_length=100)
    image = models.FileField(verbose_name=_(''), upload_to='images/')
    employee = models.ForeignKey(Employee, verbose_name=_(''), related_name='employee_documents', on_delete=models.CASCADE)
    tag = models.CharField(verbose_name=_(''), max_length=2, choices=DocumentTags.choices)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'المستندات'

    def __str__(self):
        return self.serial

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.code, allow_unicode=True)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass
        # return reverse('employees:dgree_list')

class Leave(models.Model):
    pass