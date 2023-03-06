from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages


from .models import *
from .forms import *



# Create your views here.




class SignupView(generic.View):
    def get(self, *args, **kwargs):
        context = {
            'user_creation_form': CreateUserForm(),
            'appuserform': AppUserForm()
        }
        return render(self.request, 'app_user/signup.html', context)

    def post(self, *args, **kwargs):
        userForm = CreateUserForm(data=self.request.POST)
        appUserForm = AppUserForm(data=self.request.POST)
        
        if userForm.is_valid() and appUserForm.is_valid():
            user = userForm.save(commit=False)
            # checking if the email already exists
            email_check = User.objects.filter(email=user.email)
            if email_check.count():
                messages.error(self.request, 'This email already exists. signin using the same email or choose another email.')
                return render(self.request, 'app_user/signup.html', {'user_creation_form': userForm,
                                                                 'appuserform':AppUserForm})
            else:
                user.username = user.email
                name = user.first_name
                user.first_name = name.split(' ')[0]
                user.last_name = name.split(' ')[-1]
                user.save()

                appuser = appUserForm.save(commit=False)
                appuser.user = user
                appuser.save()

                messages.success(self.request, 'Your profile was created. Login to enter into store.')
                
                return HttpResponseRedirect(reverse('app_user:signin'))
        else:
            messages.error(self.request, 'Something went wrong. Try again')
            return render(self.request, 'app_user/signup.html', {'user_creation_form': userForm,
                                                                 'appuserform':AppUserForm})
        
