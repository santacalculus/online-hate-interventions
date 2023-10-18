from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from blog.forms import LoginForm, RegisterForm, ValueForm
from blog.models import Profile, Post
from django.views.decorators.csrf import ensure_csrf_cookie
from blog.custom_backend import BlogBackend

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

# def value_action(request) :
#     context = {}
#     return render(request, 'blog/value.html', context)

@login_required
def display_action(request, id) :
    context = {}
    user = request.user
    context['posts'] = Post.objects.filter(user=user)
    context['profile'] = user.profile
    if request.method == "GET" :
        return render(request, 'blog/valuedisplay.html', context)
    
    if 'text' not in request.POST or not request.POST['text'] :
        context['error'] = 'You cannot post nothing.'
        return render(request, 'blog/valuedisplay.html', context)
    new_post = Post(text=request.POST['text'], user=request.user)
    new_post.save()
    return render(request, 'blog/valuedisplay.html', context)

@login_required
def selection_action(request, id) :
    context = {}
    user = request.user
    context['posts'] = Post.objects.filter(user=user)
    context['profile'] = user.profile
    if request.method == "GET" :
        return render(request, 'blog/usernameselection.html', context)
    
    if 'text' not in request.POST or not request.POST['text'] :
        context['error'] = 'You cannot post nothing.'
        return render(request, 'blog/usernameselection.html', context)
    new_post = Post(text=request.POST['text'], user=request.user)
    new_post.save()
    return render(request, 'blog/usernameselection.html', context)


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

    print("bro pls", form.cleaned_data['username'])
    new_user = BlogBackend().authenticate(request, username=form.cleaned_data['username'])
    
    login(request, new_user, backend='blog.custom_backend.BlogBackend')
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
    new_user = User.objects.create_user(username=form.cleaned_data['username'])
    print("New user created:", new_user.username)
    
    new_user.set_unusable_password()
    new_user.save()

    new_profile = Profile(user = new_user)
    # print("does this work", form.cleaned_data['username'])
    new_profile.save()
    print("what about now", new_profile)
    new_user = BlogBackend().authenticate(request, username=form.cleaned_data['username'])
    print("does this work", new_user)
    if new_user :
        request.user = new_user
        request._cached_user = new_user
        login(request, new_user, backend='blog.custom_backend.BlogBackend')
    print("gotcha", request.user)
    # return redirect(reverse('value'))
    return redirect(reverse('value'))



def value_action(request) :
    form = ValueForm(request.POST)
    
    if request.method == "POST" :
        
        if form.is_valid() :
            
            new_user = request.user
            print(new_user, "yes thank god")

            try:
                print("man im literally on my knees rn please")
                profile = Profile.objects.get(user=new_user)
            except Profile.DoesNotExist:
                # If the user does not have a profile, create one
                print("were here")
                profile = Profile(user=new_user)
            
            profile.interests = form.cleaned_data['interests']
            print("wtf",form.cleaned_data['value'])
            profile.value = form.cleaned_data['value']
            profile.value_importance = form.cleaned_data['value_importance']
            profile.catchphrase = form.cleaned_data['catchphrase']
            profile.save()
            all_profiles = Profile.objects.all()
            # for prof in all_profiles :
            #     print(prof.interests, "profiles so far created")
            #     print(prof.value, "values so far")
            return render(request, 'blog/success.html', {})
    else :
        return render(request, 'blog/value.html', {'form': form})
    


