from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.utils.text import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import StateForm, LocalityForm, UnityForm, CityForm, HquarterForm
from .models import State, Locality, Unity, City, Hquarter
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm

def main_locations(request):
    return render(request, 'locations/main_locations.html')

class StateCreateView(LoginRequiredMixin, CreateView):
    form_class = StateForm
    template_name = 'locations/add_state.html'
    context_object_name = 'state'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الولايات'
        context['header'] = 'أضافة ولاية جديدة'
        context['action'] = 'أضافة'
        return context

class StateListView(LoginRequiredMixin, ListView):
    model = State
    template_name = 'locations/state_list.html'
    context_object_name = 'states'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الولايات'
        context['header'] = 'قائمة الولايات'
        return context

class StateUpdateView(LoginRequiredMixin, UpdateView):
    model = State
    form_class = StateForm
    template_name = 'locations/add_state.html'
    context_object_name = 'state'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الولايات'
        context['header'] = 'تعديل ولاية -- '
        context['action'] = 'تعديل'
        return context

class StateDeleteView(LoginRequiredMixin, DeleteView):
    model = State
    template_name = 'locations/delete_state.html'
    context_object_name = 'state'
    success_url = reverse_lazy('locations:state_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الولايات'
        context['header'] = 'هل تريد حذف ولاية ---  '
        context['action'] = 'حذف'
        return context

def update_state(request, pk):
    st = get_object_or_404(State, id=pk)
    form = StateForm(request.POST or None, instance=st)
    if form.is_valid:
        form.save()
        return redirect('locations:state_list')
    else:
        raise Http404("No MyModel matches the given query.")
    return render(request, 'locations/add_state.html', {'form': form, 'action': 'تعديل'})
    # if request.method == 'POST':
    #     form = form(instance=st)
    #     form = form(request.POST)

# hquarter views
class HquarterCreateView(CreateView):
    form_class = HquarterForm
    template_name = 'locations/add_hquarter.html'
    context_object_name = 'hquarter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'أضافة رئاسة جديدة'
        context['action'] = 'أضافة'
        return context

class HquarterListView(ListView):
    model = Hquarter
    template_name = 'locations/hquarter_list.html'
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
    template_name = 'locations/add_hquarter.html'
    context_object_name = 'hquarter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'تعديل رئاسة / '
        context['action'] = 'تعديل'
        return context

class HquarterDeleteView(DeleteView):
    model = Hquarter
    template_name = 'locations/delete_hquarter.html'
    context_object_name = 'hquarter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الرئاسات'
        context['header'] = 'حذف رئاسة / '
        context['action'] = 'حذف'
        return context

# locality views
class LocalityCreateView(LoginRequiredMixin, CreateView):
    form_class = LocalityForm
    template_name = 'locations/add_locality.html'
    context_object_name = 'locality'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المحليات'
        context['header'] = 'أضافة محلية جديدة /'
        context['action'] = 'أضافة'
        return context

class LocalityListView(LoginRequiredMixin, ListView):
    model = Locality
    template_name = 'locations/locality_list.html'
    context_object_name = 'localities'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المحليات'
        context['header'] = 'قائمة المحليات'
        return context

class LocalityUpdateView(LoginRequiredMixin, UpdateView):
    model = Locality
    form_class = LocalityForm
    template_name = 'locations/add_locality.html'
    context_object_name = 'locality'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المحليات'
        context['header'] = 'تعديل محلية /'
        context['action'] = 'تعديل'
        return context

class LocalityDeleteView(LoginRequiredMixin, DeleteView):
    model = Locality
    template_name = 'locations/delete_locality.html'
    context_object_name = 'locality'
    success_url = reverse_lazy('locations:locality_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المحليات'
        context['header'] = 'حذف محلية  / '
        context['action'] = 'حذف'
        return context

# unity views
class UnityCreateView(LoginRequiredMixin, CreateView):
    form_class = UnityForm
    template_name = 'locations/add_unity.html'
    context_object_name = 'unity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الوحدات الأدارية'
        context['header'] = 'إضافة وحدة إدارية جديدة'
        context['action'] = 'إضافة'
        return context

class UnityListView(LoginRequiredMixin, ListView):
    model = Unity
    template_name = 'locations/unity_list.html'
    context_object_name = 'unities'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الوحدات الأدارية'
        context['header'] = 'قائمة الوحدات الأدارية'
        return context

class UnityUpdateView(LoginRequiredMixin, UpdateView):
    model = Unity
    form_class = UnityForm
    template_name = 'locations/add_unity.html'
    context_object_name = 'unity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الوحدات الأدارية'
        context['header'] = 'تعديل وحدة أدارية  /'
        context['action'] = 'تعديل'
        return context

class UnityDeleteView(LoginRequiredMixin, DeleteView):
    model = Unity
    template_name = 'locations/delete_unity.html'
    context_object_name = 'unity'
    success_url = reverse_lazy('locations:unity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'الوحدات الأدارية'
        context['header'] = 'قائمة الوحدات الأدارية'
        context['action'] = 'حذف'
        return context

def load_localities(request):
    state_id = int(request.GET.get('state'))
    localities = Locality.objects.filter(state_id=state_id)
    return render(request, 'snippets/load_localities.html', {'localities': localities})

# city views
class CityCreateView(LoginRequiredMixin, CreateView):
    form_class = CityForm
    template_name = 'locations/add_city.html'
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المدن'
        context['header'] ='إضافة مدينة جديدة'
        context['action'] = 'أضافة'
        return context

class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'locations/city_list.html'
    context_object_name = 'cities'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المدن'
        context['header'] ='قائمة المدن'
        return context

class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'locations/add_city.html'
    context_object_name = 'city'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المدن'
        context['header'] ='تعديل مدينة / '
        context['action'] = 'تعديل'
        return context

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'locations/delete_city.html'
    context_object_name = 'city'
    success_url = reverse_lazy('locations:city_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'المدن'
        context['header'] ='حذف مدينة / '
        context['action'] = 'حذف'
        return context

def load_unities(request):
    locality_id = int(request.GET.get('locality'))
    unities = Unity.objects.filter(locality_id=locality_id)
    return render(request, 'snippets/load_unities.html', {'unities': unities})

def load_cities(request):
    unity_id = int(request.GET.get('unity'))
    cities = City.objects.filter(unity_id=unity_id)
    return render(request, 'snippets/load_cities.html', {'cities': cities})

def search_state(request):
    search_state = request.GET.get('q')
    if search_state:
        states = State.objects.filter(name__icontains=search_state)
    else:
        states = State.objects.all()
    title = _('الولايات')
    header = _('قائمة الولايات')
    context = {
        'title': title,
        'header': header,
        'states': states
    }
    return render(request, 'locations/state_list.html', context=context)


def search_locality(request):
    search_locality = request.GET.get('q')
    if search_locality:
        localities = Locality.objects.filter(name__icontains=search_locality)
    else:
        localities = Locality.objects.all()
    title = _('المحليات')
    header = _('قائمة المحليات')
    context = {
        'title': title,
        'header': header,
        'localities': localities
    }
    return render(request, 'locations/locality_list.html', context=context)

def search_hquarter(request):
    search_hquarter = request.GET.get('q')
    if search_hquarter:
        hquarters = Hquarter.objects.filter(name__icontains=search_hquarter)
    else:
        hquarters = Hquarter.objects.all()
    title = _('الرئاسات')
    header = _('قائمة الرئاسات')
    context = {
        'title': title,
        'header': header,
        'hquarters': hquarters
    }
    return render(request, 'locations/hquarter_list.html', context=context)

def search_unity(request):
    search_unity = request.GET.get('q')
    if search_unity:
        unities = Unity.objects.filter(name__icontains=search_unity)
    else:
        unities = Unity.objects.all()
    title = _('الوحدات الإدارية')
    header = _('قائمة الوحدات الإدارية')
    context = {
        'title': title,
        'header': header,
        'unities': unities
    }
    return render(request, 'locations/unity_list.html', context=context)

def search_city(request):
    search_city = request.GET.get('q')
    if search_city:
        cities = City.objects.filter(name__icontains=search_city)
    else:
        cities = City.objects.all()
    title = _('المدن')
    header = _('قائمة المدن')
    context = {
        'title': title,
        'header': header,
        'cities': cities
    }
    return render(request, 'locations/city_list.html', context=context)
# def state_search(request):
#     form = SearchForm()
#     query = None
#     results = []
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = (State.annotate(search=SearchVector('name'),).filter(search=query))
#     title = _('الولايات')
#     header = _('قائمة الولايات')
#     context = {
#         'title': title,
#         'header': header,
#         'states': results
#     }
#     return render(request,'locations/state_list.html',context=context)
