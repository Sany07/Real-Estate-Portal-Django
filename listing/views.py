from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from .models import *

# Create your views here.



class HomeView(ListView):
    model = Property
    template_name = 'site/index.html'
    context_object_name = 'listings'

    def get_queryset(self):
        return self.model.objects.order_by('-list_date').filter(is_published=True)[:3]




def About(request):
    realtors = Realtor.objects.all()
    mvp = Mvp.objects.last()
    
    context={

        'realtors':realtors,
        'mvp':mvp

    }
    return render(request,'site/about.html',context)


class PropertyListView(ListView):
    model = Property
    template_name= 'site/listings.html'
    context_object_name = 'listings'
    paginate_by = 1

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'site/listing.html'
    context_object_name = 'property'
    pk_url_kwarg = 'id'



