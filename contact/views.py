from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Contact

class ContactView(View):

    def get(self,request, *args, **kwargs):
        return redirect('/')


    def post(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            listing_id = request.POST['listing_id']
            listing = request.POST['listing']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            message = request.POST['message']
            user_id = request.POST['user_id']

      
            if self.request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listing/'+listing_id)

            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

            contact.save()

            messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
            return redirect('/listing/'+listing_id)


