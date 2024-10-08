from django import forms
from .models import Hquarter, Sector, Office


class HquarterForm(forms.ModelForm):
    class Meta:
        model = Hquarter
        fields = ['name', 'state']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control py-1 smf border-0 border-bottom border-success rounded-0',
                'placeholder': 'اسم الأمانة'
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'class': 'form-control py-1 smf border-0 border-bottom border-success rounded-0',
                'placeholder': ''
            }
        )

class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector
        fields = ['name', 'state', 'hquarter']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['name'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                    'placeholder': 'اسم القطاع'
                }
            )
        self.fields['state'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                }
            )
        self.fields['hquarter'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                }
            )
        self.fields['hquarter'].queryset = Hquarter.objects.none()
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('hquarter'))
                self.fields['hquarter'].queryset = Hquarter.objects.filter(state_id=state_id)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['hquarter'].queryset = self.instance.state.state_hquarters

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['name', 'state', 'hquarter', 'sector']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['name'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                    'placeholder': 'اسم القطاع'
                }
            )
        self.fields['state'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                }
            )
        self.fields['hquarter'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                }
            )
        self.fields['sector'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf border-0 border-success border-bottom rounded-0',
                }
            )

        self.fields['hquarter'].queryset = Hquarter.objects.none()
        self.fields['sector'].queryset = Sector.objects.none()


        if 'state' in self.data:
            try:
                state_id = int(self.data.get('hquarter'))
                self.fields['hquarter'].queryset = Hquarter.objects.filter(state_id=state_id)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['hquarter'].queryset = self.instance.state.state_hquarters

        if 'hquarter' in self.data:
            try:
                hquarter_id = int(self.data.get('hquarter'))
                self.fields['sector'].queryset = Sector.objects.filter(hquarter_id=hquarter_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sector'].queryset = self.instance.hquarter.hquarter_sectors
