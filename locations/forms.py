from django import forms
from .models import State, Locality, Unity, City, Hquarter


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['name'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',
                    'placeholder': 'أدخل الولاية'
                }
            )

class SearchForm(forms.Form):
    query = forms.CharField()

# hquarter form
class HquarterForm(forms.ModelForm):
    class Meta:
        model = Hquarter
        fields = ['name', 'state']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',
                'placeholder': 'ادخل الرئاسة',
            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',

            }
        )

# locality form
class LocalityForm(forms.ModelForm):
    class Meta:
        model = Locality
        fields = ['state', 'name']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['state'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50'
                }
            )
        self.fields['name'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',
                    'placeholder': 'أدخل المحلية'
                }
            )


class UnityForm(forms.ModelForm):
    class Meta:
        model = Unity
        fields = ['name', 'state', 'locality']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['state'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',

                }
            )
        self.fields['locality'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',

                }
            )
        self.fields['name'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',
                    'placeholder': 'أدخل الوحدة الإدارية'

                }
            )


        self.fields['locality'].queryset = Locality.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['locality'].queryset = Locality.objects.filter(
                    state_id=state_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['locality'].queryset = self.instance.state.state_localities


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'state', 'locality', 'unity']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['state'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50'
                }
            )
        self.fields['locality'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50'
                }
            )
        self.fields['unity'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50'
                }
            )
        self.fields['name'].widget.attrs.update(
                {
                    'class': 'form-control py-1 smf rounded-0 border-0 border-bottom border-primary border-opacity-50',
                    'placeholder': 'أدخل المدينة'

                }
            )

        self.fields['locality'].queryset = Locality.objects.none()
        self.fields['unity'].queryset = Unity.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['locality'].queryset = Locality.objects.filter(
                    state_id=state_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['locality'].queryset = self.instance.state.state_localities

        if 'locality' in self.data:
            try:
                locality_id = int(self.data.get('locality'))
                self.fields['unity'].queryset = Unity.objects.filter(
                    locality_id=locality_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['unity'].queryset = self.instance.locality.locality_unities
