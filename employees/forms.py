# import djhacker
from django.forms import ClearableFileInput
from django import forms
from .models import Dgree, Range, Bonus, Employee
from locations.models import State, Locality, Unity, City
from offices.models import Hquarter, Sector, Office
from .models import Document
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField
from dal import autocomplete


class DateInput(forms.DateInput):
    input_type = 'date'

class RangeForm(forms.ModelForm):
    class Meta:
        model = Range
        fields = [
            'name'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control border-0 border-bottom border-primary rounded-0 smf',
                'placeholder': 'القطاع'
            }
        )

class BonusForm(forms.ModelForm):
    class Meta:
        model = Bonus
        fields = [
            'name'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control border-0 border-bottom border-primary rounded-0 smf',
                'placeholder': 'العلاوة'
            }
        )

class DgreeForm(forms.ModelForm):
    class Meta:
        model = Dgree
        fields = [
                    'name', 'section', 'bonus', 'base_salary', 'begin_date', 'monthly_add', 'yearly_add', 'emp_type'
                ]
        widgets = {
            'begin_date' : DateInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control py-1  border-secondary smf',
            }
        )
        self.fields['section'].widget.attrs.update(
            {
                'class': 'form-control py-1 b border-secondary smf',
            }
        )
        self.fields['bonus'].widget.attrs.update(
            {
                'class': 'form-control py-1 border-secondary smf',
            }
        )
        self.fields['base_salary'].widget.attrs.update(
            {
                'class': 'form-control py-1  border-secondary smf',
            }
        )
        self.fields['begin_date'].widget.attrs.update(
            {
                'class': 'form-control py-1  border-secondary smf',
                'widget' : DateInput
            }
        )
        self.fields['monthly_add'].widget.attrs.update(
            {
                'class': 'form-control py-1  border-secondary smf',
            }
        )
        self.fields['yearly_add'].widget.attrs.update(
            {
                'class': 'form-control py-1  border-secondary smf',
            }
        )
        self.fields['emp_type'].widget.attrs.update(
            {
                'class': 'form-control py-1  border-secondary smf',
            }
        )


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class FileFieldForm(forms.Form):
    # file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    file_field = MultipleFileField()


# class FileFieldForm(forms.Form):
#     file_field = MultipleFileField()

class EmployeeForm(forms.ModelForm):
    # documents = MultipleFileField(widget=MultipleFileInput())
    # documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    # documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    # image = forms.ImageField(widget=ClearableFileInput(attrs={'multiple':True}))
    # image = MultipleFileField(label='الصورة', required=False)
    # documents = MultipleFileField(label='المرفقات', required=False)
    class Meta:
        model = Employee
        fields = [
            'idn', 'name','image', 'national_no', 'birth_date', 'state', 'locality', 'unity', 'city', 'address',
            'hquarter', 'sector', 'office', 'dgree', 'maritial_status', 'wives_no',
            'sons_no', 'education', 'employee_type', 'documents'
        ]
        widgets = {
                    'birth_date' : DateInput,
                    # 'documents': forms.ClearableFileInput(attrs={'allow_multiple_selected': True})
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control py-1 border-0 rounded-0 border-bottom border-success smf'
                }
            )
        self.fields['birth_date'].widget.attrs.update(
                {
                    'widget' : DateInput
                }
        )

        self.fields['locality'].queryset = Locality.objects.none()
        self.fields['unity'].queryset = Unity.objects.none()
        self.fields['city'].queryset = City.objects.none()
        # current work
        self.fields['sector'].queryset = Sector.objects.none()
        self.fields['office'].queryset = Office.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['locality'].queryset = Locality.objects.filter(state_id=state_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['locality'].queryset = self.instance.state.state_localities

        # unity dropdown
        if 'locality' in self.data:
            try:
                locality_id = int(self.data.get('locality'))
                self.fields['unity'].queryset = Unity.objects.filter(locality_id=locality_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['unity'].queryset = self.instance.locality.locality_unities

        # city dropdown
        if 'unity' in self.data:
            try:
                unity_id = int(self.data.get('unity'))
                self.fields['city'].queryset = City.objects.filter(unity_id=unity_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.unity.unity_cities

        # current locality dropdown
        if 'hquarter' in self.data:
            try:
                hquarter_id = int(self.data.get('hquarter'))
                self.fields['sector'].queryset = Sector.objects.filter(hquarter_id=hquarter_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sector'].queryset = self.instance.hquarter.hquarter_sectors

        # current unity dropdown
        if 'sector' in self.data:
            try:
                sector_id = int(self.data.get('sector'))
                self.fields['office'].queryset = Office.objects.filter(sector_id=sector_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['office'].queryset = self.instance.sector.sector_offices

# Document Form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['employee', 'image', 'tag']
        # widgets = {
        #     'employee': autocomplete.ModelSelect2(url='employees:EmployeeAutocomplete', attrs={'data-html': True})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update(
                {
                    'class': 'form-control py-1 border-0 border-bottom rounded-0 smf',
                    'placeholder': 'الصورة'
                }
            )
        self.fields['employee'].widget.attrs.update(
                {
                    'class': 'form-control py-1 border-0 border-bottom rounded-0 smf',
                }
        )
        self.fields['tag'].widget.attrs.update(
                {
                    'class': 'form-control py-1 border-0 border-bottom rounded-0 smf',
                    'placeholder': 'نوع المستند'
                }
        )

# djhacker.formfield(
#     Document.employee,
#     forms.ModelChoiceField,
#     widget=autocomplete.ModelSelect2(url='employees:EmployeeAutocomplete')
# )
