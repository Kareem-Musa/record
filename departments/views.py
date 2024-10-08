from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.apps import apps
from django.forms.models import modelform_factory
from .forms import PlanningForm, DepartmentForm
from .models import Planning, Department

class PlanningCreateView(CreateView):
    form_class = PlanningForm
    template_name = 'departments/add_planning.html'
    context_object_name = 'planning'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('قائمة الإدارات التخطيطية')
        context['header'] = _('إضافة إدارة تخطيطية')
        context['action'] = _('إضافة')
        return context

class PlanningListView(ListView):
    model = Planning
    template_name = 'departments/planning_list.html'
    context_object_name = 'plannings'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('قائمة الإدارات التخطيطية')
        context['header'] = _('الإدارات')
        return context

class PlanningUpdateView(UpdateView):
    model = Planning
    form_class = PlanningForm
    template_name = 'departments/add_planning.html'
    context_object_name = 'planning'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('قائمة الإدارات التخطيطية')
        context['header'] = _('تعديل الإدارة')
        context['action'] = _('تعديل')
        return context

class PlanningDeleteView(DeleteView):
    model = Planning
    template_name = 'departments/delete_planning.html'
    context_object_name = 'planning'
    success_url = reverse_lazy('departments:planning_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('قائمة الإدارات التخطيطية')
        context['header'] = _('إضافة إدارة تخطيطية')
        context['action'] = _('إضافة')
        return context

# Department views
class DepartmentCreateView(CreateView):
    form_class = DepartmentForm
    template_name = 'departments/add_department.html'
    context_object_name = 'department'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الإدارات')
        context['header'] = _('إضافة إدارة')
        context['action'] = _('إضافة')
        return context

class DepartmentListView(ListView):
    model = Department
    template_name = 'departments/department_list.html'
    context_object_name = 'departments'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الإدارات')
        context['header'] = _('قائمة الإدارات')
        return context


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'departments/add_department.html'
    context_object_name = 'department'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الإدارات')
        context['header'] = _('تعديل إدارة')
        context['action'] = _('تعديل')
        return context

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'departments/delete_department.html'
    context_object_name = 'department'
    success_url = reverse_lazy('departments:department_list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = _('الإدارات')
        context['header'] = _('تعديل إدارة')
        context['action'] = _('حذف')
        return context

# create department
class DepartmentCreateUpdateView(TemplateResponseMixin, View):
    management = None
    model = None
    obj = None
    template_name = 'departments/add_department.html'

    def get_model(self, model_name):
        if model_name in ['state', 'locality', 'unity']:
            return apps.get_model(
                app_label='courses', model_name=model_name
            )
        return None

    def get_form(self, model, *args, **kwargs):
        Form = modelform_factory(
            model, exclude=['slug', 'created', 'updated']
        )
        return Form(*args, **kwargs)

    def dispatch(self, request, management_id, model_name, id=None):
        self.management = get_object_or_404(
            Management, id=management_id
        )
        self.model = self.get_model(model_name)
        if id:
            self.obj = get_object_or_404(
                self.model, id=id
            )
        return super().dispatch(request, management_id, model_name, id)

    def get(self, request, management_id, model_name, id=None):
        form = self.get_form(self.model, instance=self.obj)
        return self.render_to_response(
            {'form': form, 'object': self.obj}
        )

    def post(self, request, management_id, model_name, id=None):
        form = self.get_form(
            self.model,
            instance=self.obj,
            data=request.POST,
            files=request.FILES,
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            if not id:
                # new content
                Content.objects.create(management=self.management, item=obj)
            return redirect('management_department_list', self.management.id)
        return self.render_to_response(
            {'form': form, 'object': self.obj}
        )
