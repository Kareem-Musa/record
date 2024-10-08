from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import HquarterForm, SectorForm, OfficeForm
from .models import Hquarter, Sector, Office

class HquarterCreateView(CreateView):
    form_class = HquarterForm
    template_name = 'offices/add_hquarter.html'
    context_object_name = 'hquarter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'أضافة رئاسة جديدة'
        context['action'] = 'أضافة'
        return context

class HquarterListView(ListView):
    model = Hquarter
    template_name = 'offices/hquarter_list.html'
    context_object_name = 'hquarters'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'قائمة الرئاسات'
        return context

class HquarterUpdateView(UpdateView):
    model = Hquarter
    form_class = HquarterForm
    template_name = 'offices/add_hquarter.html'
    context_object_name = 'hquarter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'تعديل رئاسة / '
        context['action'] = 'تعديل'
        return context

class HquarterDeleteView(DeleteView):
    model = Hquarter
    template_name = 'offices/delete_hquarter.html'
    context_object_name = 'hquarter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'حذف رئاسة / '
        context['action'] = 'حذف'
        return context

# sector views
class SectorCreateView(CreateView):
    form_class = SectorForm
    template_name = 'offices/add_sector.html'
    context_object_name = 'sector'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'القطاعات'
        context['header'] = 'أضافة قطاع جديد'
        context['action'] = 'أضافة'
        return context

class SectorListView(ListView):
    model = Sector
    template_name = 'offices/sector_list.html'
    context_object_name = 'sectors'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'القطاعات'
        context['header'] = 'قائمة القطاعات'
        return context

class SectorUpdateView(UpdateView):
    model = Sector
    form_class = SectorForm
    template_name = 'offices/add_sector.html'
    context_object_name = 'sector'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'القطاعات'
        context['header'] = 'تعديل قطاع / '
        context['action'] = 'تعديل'
        return context

class SectorDeleteView(DeleteView):
    model = Sector
    template_name = 'offices/delete_sector.html'
    context_object_name = 'sector'
    success_url = reverse_lazy('offices:sector_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'القطاعات'
        context['header'] = 'حذف قطاع / '
        context['action'] = 'تأكيد'
        return context

# load hquarters
def load_hquarters(request):
    state_id = int(request.GET.get('state'))
    hquarters = Hquarter.objects.filter(state_id=state_id)
    return render(request, 'snippets/load_hquarters.html', {'hquarters': hquarters})
# office views
class OfficeCreateView(CreateView):
    form_class = OfficeForm
    template_name = 'offices/add_office.html'
    context_object_name = 'office'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المكاتب'
        context['header'] = 'أضافة مكتب جديد'
        context['action'] = 'أضافة'
        return context

class OfficeListView(ListView):
    model = Office
    template_name = 'offices/office_list.html'
    context_object_name = 'offices'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المكاتب'
        context['header'] = 'قائمة المكاتب'
        return context

class OfficeUpdateView(UpdateView):
    model = Office
    form_class = OfficeForm
    template_name = 'offices/add_office.html'
    context_object_name = 'office'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المكاتب'
        context['header'] = 'تعديل مكتب / '
        context['action'] = 'تعديل'
        return context

class OfficeDeleteView(DeleteView):
    model = Office
    template_name = 'offices/delete_office.html'
    context_object_name = 'office'
    success_url = reverse_lazy('offices:office_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المكاتب'
        context['header'] = 'حذف مكتب / '
        context['action'] = 'حذف'
        return context

# load sectors
def load_sectors(request):
    hquarter_id = int(request.GET.get('hquarter'))
    sectors = Sector.objects.filter(hquarter_id=hquarter_id)
    return render(request, 'snippets/load_sectors.html', {'sectors': sectors})

# load offices
def load_offices(request):
    sector_id = int(request.GET.get('sector'))
    offices = Office.objects.filter(sector_id=sector_id)
    return render(request, 'snippets/load_offices.html', {'offices': offices})

# search office
def search_office(request):
    search_text = request.GET.get('q')
    if search_text:
        offices = Office.objects.filter(name__icontains=search_text)
    else:
        offices = Office.ojects.all()
    context = {
        'title': _('المكاتب'),
        'header': _('قائمة المكاتب'),
        'offices': offices
    }
    return render(request, 'offices/office_list.html', context=context)
