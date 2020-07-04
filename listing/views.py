from django.shortcuts import render
from django.views.generic import CreateView , DetailView, ListView  , TemplateView

from .models import *

class HomeView(ListView):
    model = Property
    template_name = 'site/index.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return self.model.objects.order_by('-list_date').filter(is_published=True)[:3]

class PropertyListView(ListView):
    model = Property
    template_name= 'site/listings.html'
    context_object_name = 'listings'
    paginate_by = 10

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'site/listing.html'
    context_object_name = 'property'
    pk_url_kwarg = 'id'


class AboutView(TemplateView):
    template_name = 'site/about.html'

    def get_context_data(self, **kwargs):
         context = super(AboutView, self).get_context_data(**kwargs)
         context['realtors'] = Realtor.objects.all()
         context['mvp'] = Mvp.objects.last()
         return context
