from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User

from contact.models import Contact
# Create your views here.


class RegisterView(CreateView):
    """
        Provides the ability to Register
    """
    model = User
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('listing:home')
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Register Successfull')
            return redirect('account:login')
        else:
            return render(request, 'account/register.html', {'form': form})




def dashboard(request):
    return render(request,'account/dashboard.html')


class LoginView(FormView):
    """
        Provides the ability to login as a user with an username and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))    


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/account/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class DashBoardView(LoginRequiredMixin, ListView):
    """
    Provides users the ability to view his contact list
    """
    model = Contact
    template_name = "account/dashboard.html"
    context_object_name = 'contacts'
    login_url = '/account/login'


    def get_queryset(self):
        return self.model.objects.order_by('-contact_date').filter(user_id=self.request.user.id)

