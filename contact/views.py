from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
# Create your views here.
from .models import Contact


class ContactView(View):
    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            listing_id = request.POST['listing_id']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            # realtor_email = request.POST['realtor_email']

            #  Check if user has made inquiry already
            if self.request.user.is_authenticated:
                id = request.user.id
                # user_name = get_object_or_404(User, id=id)
                has_contacted = Contact.objects.filter(listing_id=listing_id, user_name=id)
                if has_contacted:
           
                    return redirect('/listing/'+listing_id)

            contact = Contact(user_name_id=id, listing_id=listing_id, email=email, message=message,  phone=phone )
            contact.save()

            return redirect('/')

    def get(self,request, *args, **kwargs):
        return redirect('/')