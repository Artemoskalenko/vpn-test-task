from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class LoginUser(LoginView):
    """Class that generates the login page"""
    form_class = AuthenticationForm
    template_name = 'user/login_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(
            form=form,
            message='Invalid username and/or password.'))

    def get_success_url(self):
        return reverse_lazy('profile')


def register(request):
    """
    Function that generates the registration page.
    With the POST method, it receives data from the registration form, creates a new user and redirects him to the 'profile' page
    """
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'user/register.html', {
                'message': 'Passwords must match.',
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'user/register.html', {
                'message': 'Username already taken.',
            })
        login(request, user)
        return HttpResponseRedirect(reverse('profile'))
    else:
        return render(request, 'user/register.html')


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        # changing user data
        user = User.objects.get(id=request.user.id)
        if request.POST['username']:
            user.username = request.POST['username']
        if request.POST['first_name']:
            user.first_name = request.POST['first_name']
        if request.POST['last_name']:
            user.last_name = request.POST['last_name']
        if request.POST['email']:
            user.email = request.POST['email']
        user.save()
        return redirect('profile')

    return render(request, 'user/profile.html')


def index(request):
    return redirect('login')
