from django import forms
from .models import Planning, Department

class PlanningForm(forms.ModelForm):
    class Meta:
        model = Planning
        fields = [
            'name', 'state', 'top_management'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control py-1 border-0 border-bottom rounded-0 border-primary',

            }
        )
        self.fields['state'].widget.attrs.update(
            {
                'class': 'form-control py-1 border-0 border-bottom rounded-0 border-primary',
            }
        )
        self.fields['top_management'].widget.attrs.update(
            {
                'class': 'form-control py-1 border-0 border-bottom rounded-0 border-primary',
            }
        )

# Dept form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name', 'management', 'min_dgree'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {
                'class': 'form-control py-1 rounded-0 border-0 border-bottom border-secondary border-2 border-opacity-50 smf',
                'placeholder': 'الإدارة'

            }
        )
        self.fields['management'].widget.attrs.update(
            {
                'class': 'form-control py-1 rounded-0 border-0 border-bottom border-secondary border-2 border-opacity-50 smf',
            }
        )
        self.fields['min_dgree'].widget.attrs.update(
            {
                'class': 'form-control py-1 rounded-0 border-0 border-bottom border-secondary border-2 border-opacity-50 smf',
            }
        )
