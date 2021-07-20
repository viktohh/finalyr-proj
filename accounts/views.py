from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render
from django.urls import reverse




def lecturer_signup(request):
    # user.is_lecturer = True
    pass

def student_signup(request):
    message = ""
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data["username"]
            email = user_form.cleaned_data["email"]
            if get_user_model().objects.filter(username=username).exists():
                messages.error(request, "A user with that username already exists.")
            elif get_user_model().objects.filter(email=email).exists():
                messages.error(request, "A get_user_model() with that email address already exists.")
            else:
                user = user_form.save()
                login(request, user)
                messages.success(request, "get_user_model() was successfully created.")
                return redirect("complete-profile")
    else:
        user_form = UserForm()
    context = {"user_form": user_form}
    return render(request, "accounts/lecturer_signup.html", context)


def sign_in(request):
    login_form = LoginForm(request.POST or None)
    if request.method == "POST":
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "User was successfully logged in.")
                return redirect("/dashboard")
            else:
                messages.error(request, "Username or password is incorrect")
        else:
            messages.error(request, "Form is not valid")
    context = {"login": login_form}
    return render(request, "accounts/sign_in.html", context=context)

    @login_required(login_url="sign_in")






