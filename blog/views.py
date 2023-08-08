from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from blog.forms import LoginForm, RegisterForm
from blog.models import Profile, Post
from django.views.decorators.csrf import ensure_csrf_cookie

@login_required
# Create your views here.
def base_action(request) :
    context = {}
    user = request.user
    context['posts'] = Post.objects.filter(user=user)
    context['profile'] = user.profile
    if request.method == "GET" :
        return render(request, 'blog/page.html', context)
    
    if 'text' not in request.POST or not request.POST['text'] :
        context['error'] = 'You cannot post nothing.'
        return render(request, 'blog/page.html', context)
    new_post = Post(text=request.POST['text'], user=request.user)
    new_post.save()
    return render(request, 'blog/page.html', context)


def login_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'blog/login.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = LoginForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'blog/login.html', context)

    
    login(request, new_user)
    return redirect('page')

def logout_action(request):
    logout(request)
    return redirect(reverse('login'))


def register_action(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegisterForm()
        return render(request, 'blog/signup.html', context)

    # Creates a bound form from the request POST parameters and makes the 
    # form available in the request context dictionary.
    form = RegisterForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'blog/signup.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'], 
                                        password=form.cleaned_data['password'])
    new_user.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    new_profile = Profile(user = new_user)
    new_profile.save()
    login(request, new_user)
    return redirect(reverse('page'))


# def post_action(request):
#     context = {}
#     user = request.user
#     context['posts'] = Post.objects.all()
#     context['profile'] = user.profile
#     if request.method == "GET" :
#         return render(request, 'blog/page.html', context)
    
#     if 'text' not in request.POST or not request.POST['text'] :
#         context['error'] = 'You cannot post nothing.'
#         return render(request, 'blog/page.html', context)
#     new_post = Post(text=request.POST['text'], user=request.user)
#     new_post.save()
#     return render(request, 'blog/page.html', context)
