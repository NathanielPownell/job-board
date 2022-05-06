from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, RegisterEmployerForm

# def loginView(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return(HttpResponse('Logged In'))
#     else:
#         return(HttpResponse('Invalid Login'))

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/profile/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})


def registerEmployer(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/settings/employer/")
    else:
        register_form = RegisterForm()
        employer_form = RegisterEmployerForm()

    return render(response, "register/register_employer.html", {"register_form": register_form, "employer_form": employer_form})

    