from django.shortcuts import redirect, render
from .forms import UserRegisterForm, UserLoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group

# Home 
def home(request):
    posts = Post.show_posts()
    return render(request, 'app/home.html',{ 'posts': posts})

# About 
def about(request):
    return render(request, 'app/about.html')

# Contact 
def contact(request):
    return render(request, 'app/contact.html')

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.show_posts()
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()
        return render(request, 'app/dashboard.html', {
             'posts': posts ,
             'full_name': full_name,
             'groups': groups
            })
    else:
        return redirect('login')

# Add Post
def addPost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Posts added successfully.')
                return redirect('dashboard')
        else:
            form = PostForm()
            return render(request,'app/addPost.html', { 'form': form })

    else:
        return redirect('login')

# Delete Post
def deletePost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.get_post(id)
            post.delete()
            return redirect('dashboard')
    else:
        return redirect('login')

#Edit Post
def editPost(request, id):
    if request.user.is_authenticated:
        post = Post.get_post(id)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully.')
                return redirect('dashboard')
        else:
            form = PostForm(instance=post)
            return render(request, 'app/editPost.html', { 'form': form })
    else:
        return redirect('login')

# Register 
def userRegister(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='Author')
                user.groups.add(group)
                messages.success(request, 'Congractulations! You have become an Author. Now please Login')
                return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request, 'app/register.html', { 'form': form })
    else:
        return redirect('dashboard')

# Login 
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get('username')
                upass = form.cleaned_data.get('password')
                user = authenticate(username=uname, password=upass)
                print(user)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return redirect('dashboard')
        else:
            form = UserLoginForm()
            return render(request, 'app/login.html', { 'form': form })
    else:
        return redirect('dashboard')

# Logout 
def userLogout(request):
    logout(request)
    return redirect('home')

