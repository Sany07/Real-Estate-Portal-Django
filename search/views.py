from django.views.generic import ListView
from listing.models import Property
# Create your views here.



class SearchView(ListView):
    model = Property 
    template_name = "site/search.html"
    context_object_name = 'listings'
    paginate_by = 20
    
    def get_queryset(self):

        if 'keywords' in self.request.GET:
            keywords = self.request.GET['keywords']

            if keywords:
                return self.model.objects.filter(description__icontains=keywords)

        # City
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city:
                print(city)

                return self.model.objects.filter(city__iexact=city)

        # State
        if 'state' in self.request.GET:
            state = self.request.GET['state']
            if state:
                return self.model.objects.filter(state__iexact=state)

        # Bedrooms
        if 'bedrooms' in self.request.GET:
     
            bedrooms = self.request.GET['bedrooms']
            if bedrooms:
                return self.model.objects.filter(bedrooms__iexact=bedrooms)

        # Price
        if 'price' in self.request.GET:
            price = self.request.GET['price']
            if price:
                return self.model.objects.filter(price__lte=price)






