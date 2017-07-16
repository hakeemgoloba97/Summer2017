from django.shortcuts import render
from mainApp.forms import userInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'mainApp/index.html')

@login_required
def movieRate(request):
    return render(request,'mainApp/movieRate.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def signup(request):
    registered = False

    if request.method == "POST":
        user_form = userInfoForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

    else:
        user_form = userInfoForm

    return  render(request, 'mainApp/SignUp.html',
                        {'user_form':user_form,
                         'registered':registered})



def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password =password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("failed log in")
            return HttpResponse("Didnt work")
    else:
        return render(request,'mainApp/login.html',{})
