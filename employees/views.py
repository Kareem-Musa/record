from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import RangeForm, BonusForm, DgreeForm, EmployeeForm, DocumentForm
from .models import Range, Bonus, Dgree, Employee, Document
from locations.models import Locality, Unity
from django.forms.models import modelformset_factory
from dal import autocomplete
from datetime import datetime


class RangeCreateView(CreateView):
    form_class = RangeForm
    template_name = 'employees/add_range.html'
    context_object_name = 'range'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('القطاعات')
        context['header'] = _('أضافة قطاع جديد')
        context['action'] = _('إضافة   القطاع')
        return context

class RangeListView(ListView):
    model = Range
    template_name = 'employees/range_list.html'
    context_object_name = 'ranges'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('القطاعات')
        context['header'] = _('قائمة القطاعات')
        return context

class RangeUpdateView(UpdateView):
    model = Range
    form_class = RangeForm
    template_name = 'employees/add_range.html'
    context_object_name = 'range'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('القطاعات')
        context['header'] = _('تعديل قطاع')
        context['action'] = _('تعديل')
        return context

class RangeDeleteView(DeleteView):
    model = Range
    template_name = 'employees/delete_range.html'
    context_object_name = 'range'
    success_url = reverse_lazy('employess:range_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('القطاعات')
        context['header'] = _('أضافة قطاع جديد')
        context['action'] = _('أضافة')
        return context

# Bonus views
class BonusCreateView(CreateView):
    form_class = BonusForm
    template_name = 'employees/add_bonus.html'
    context_object_name = 'bonus'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('العلاوات')
        context['header'] = _('إضافة علاوة جديد')
        context['action'] = _('إضافة')
        return context

class BonusListView(ListView):
    model = Bonus
    template_name = 'employees/bonus_list.html'
    context_object_name = 'bonuses'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('العلاوات')
        context['header'] = _('قائمة العلاوات')
        return context

class BonusUpdateView(UpdateView):
    model = Bonus
    form_class = BonusForm
    template_name = 'employees/add_bonus.html'
    context_object_name = 'bonus'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('العلاوات')
        context['header'] = _('تعديل علاوة')
        context['action'] = _('تعديل')
        return context

class BonusDeleteView(DeleteView):
    model = Bonus
    template_name = 'employees/delete_bonus.html'
    context_object_name = 'bonus'
    success_url = reverse_lazy('employess:bonus_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('العلاوات')
        context['header'] = _('حذف علاوة جديدة')
        context['action'] = _('حذف')
        return context

# Dgree views
def create_dgree(request):
    if request.method == 'POST':
        form = DgreeForm(request.POST)
        if form.is_valid():
            dg = form.save()
            dg.tag = str()

class DgreeCreateView(CreateView):
    form_class = DgreeForm
    template_name = 'employees/add_dgree.html'
    context_object_name = 'dgree'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الدرجات')
        context['header'] = _('إضافة درجة جديدة')
        context['action'] = _('إضافة الدرجة')
        return context

class DgreeListView(ListView):
    model = Dgree
    template_name = 'employees/dgree_list.html'
    context_object_name = 'dgrees'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الدرجات')
        context['header'] = _('قائمة الدرجات')
        return context

class DgreeUpdateView(UpdateView):
    model = Dgree
    form_class = DgreeForm
    template_name = 'employees/add_dgree.html'
    context_object_name = 'dgree'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الدرجات')
        context['header'] = _('تعديل درجة')
        context['action'] = _('تعديل')
        return context

class DgreeDeleteView(DeleteView):
    model = Dgree
    template_name = 'employees/delete_dgree.html'
    context_object_name = 'dgree'
    success_url = reverse_lazy('employess:dgree_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الدرجات')
        context['header'] = _('حذف درجة')
        context['action'] = _('حذف')
        return context

# Employee views
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        path = settings.MEDIA_ROOT
        if form.is_valid():
            emp = form.save(commit=False)
            uploaded_files = request.FILES.getlist('documents')
            for image in uploaded_files:
                path += image.name
                with open(path, 'wb') as fp:
                    for chunck in f.chunck():
                        fp.write()
                emp.documents = image
                # emp.save(commit=True)
            # emp.documents = files
            # emp.save()
            # emp.save()
            # for i in images:
            #     Employee.objects.create(image = i)
            emp.save()
            return redirect('employees:employee_list')
        else:
            pass
    else:
        form = EmployeeForm()
    title = _('الموظفين')
    header = _('أضافة موظف')
    action = _('إضافة الوظف')
    context = {
        'form': form,
        'title': title,
        'header': header,
        'action': action
    }
    return render(request, 'employees/add_employee.html', context=context)

def update_employee(request, pk):
    emp = Employee.objects.get(id=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=emp)
        if form.is_valid():
            emp = form.save(commit=False)
            for image in request.FILES.getlist('documents'):
                emp.documents = image
                # emp.save(commit=True)
            # do something
            emp.save()
            return redirect('employees:employee_list')
        else:
            pass
    else:
        form = EmployeeForm(instance=emp)
    title = _('الموظفين')
    header = _('تعديل موظف')
    action = _('تعديل بيانات الموظف')
    context = {
        'form': form,
        'title': title,
        'header': header,
        'action': action
    }
    return render(request, 'employees/add_employee.html', context=context)

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الموظفين')
        context['header'] = _('قائمة الموظفين')
        return context

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/delete_employee.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employees:employee_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الموظفين')
        context['header'] = _('قائمة الموظفين')
        context['action'] = _('حذف الموظف')
        return context

# dropdowns
def load_current_localities(request):
    state_id = int(request.GET.get('current_state'))
    localities = Locality.objects.filter(state_id=state_id)
    return render(request, 'snippets/load_current_localities.html', {'localities': localities})

def load_current_unities(request):
    locality_id = int(request.GET.get('current_locality'))
    unities = Unity.objects.filter(locality_id=locality_id)
    return render(request, 'snippets/load_current_unities.html', {'unities': unities})

# search  Employee
def search_employee(request):
    search_text = request.GET.get('q')
    if search_text:
        employees = Employee.objects.filter(name__icontains=search_text)
    else:
        employees = Employee.objects.all()
    context = {
        'title': _('الموظفين'),
        'header': _('قائمة الموظفين'),
        'employees': employees
    }
    return render(request, 'employees/employee_list.html', context=context)

# print Employee Info
def print_employee(request):
    pass

# Document views
def create_document(request):
    if request.method == 'POST':
        formset = DocumentForm(request.POST, request.FILES)
        # emp = formset.employee
        if formset.is_valid():
            document = formset.save(commit=False)
            name = document.employee.name
            date = datetime.today().strftime("%Y%m%d")
            document.save()
            document.code = ((str(date) +"_"+ str(document.id)))
            document.save()
            return redirect('employees:document_list')
        else:
            print (formset.errors)
    else:
        formset = DocumentForm()
    context = {
        'title': _('المرفقات'),
        'header': _('أضافة مرفق'),
        'action': _('إضافة'),
        'form': formset
    }
    return render(request, 'employees/add_document.html', context=context)

class EmployeeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Employee.objects.none()

        qs = Employee.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

class DocumentListView(ListView):
    model = Document
    template_name = 'employees/document_list.html'
    context_object_name = 'documents'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('المرفقات')
        context['header'] = _('قائمة المرفقات')
        return context
