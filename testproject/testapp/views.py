from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_user(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:  # if user exist
    #         login(request, user)
    #         return redirect('index') 
    #     else:
    #         return redirect('')  
    # else:
        return render(request, 'login.html', )
    

def index(request):
    return render(request, 'index.html')

def register_user(request):
    return render(request, 'registration.html')


def logout_user(request):
    logout(request)
    return redirect('/')


# from django.http import HttpResponseRedirect
# from django.shortcuts import render

# from .forms import NameForm


# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect("/thanks/")

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, "name.html", {"form": form})