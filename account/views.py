from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request,'account/register.html')


def login(request):
    return render(request,'account/login.html')


def dashboard(request):
    return render(request,'account/dashboard.html')


# class LoginView(FormView):
#     """
#         Provides the ability to login as a user with an email and password
#     """
#     success_url = '/'
#     form_class = UserLoginForm
#     template_name = 'account/login.html'

#     extra_context = {
#         'title': 'Login'
#     }

#     def dispatch(self, request, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())
#         return super().dispatch(self.request, *args, **kwargs)

#     def get_success_url(self):
#         if 'next' in self.request.GET and self.request.GET['next'] != '':
#             return self.request.GET['next']
#         else:
#             return self.success_url

#     def get_form_class(self):
#         return self.form_class

#     def form_valid(self, form):
#         auth.login(self.request, form.get_user())
#         return HttpResponseRedirect(self.get_success_url())

#     def form_invalid(self, form):
#         """If the form is invalid, render the invalid form."""
#         return self.render_to_response(self.get_context_data(form=form))    