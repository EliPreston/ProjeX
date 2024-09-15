from django.shortcuts import render, redirect 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Project, ProjectMaterial
from .forms import ProjectCreationForm, SignUpForm


def userlogin(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an issue logging you in, please make sure you are using the right username/password")
            return redirect('login')
    
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'userlogin.html', {})


def userlogout(request):
    logout(request)
    return redirect('home')


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')


    return render(request, 'signup.html', {'form': form})


def home(request):
    projects = Project.objects.filter(visibility="PUBLIC")
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'home.html', {"user": user, "projects": projects})
    else:
        return render(request, 'home.html', {"projects": projects})


def profilelist(request):
    if request.user.is_authenticated and request.user.username == "admin":
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profilelist.html', {"profiles": profiles})
    else:
        # message.success(request, "You musst be logged in as an admin to view this page...")
        return redirect('home')


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        currentuserprofile = Profile.objects.get(user_id=request.user.id)
        projects = Project.objects.filter(user_id=pk).order_by("-time_created")

        # Post form logic
        if request.method == "POST":
            # Get current
            curr_user_profile = request.user.profile
            # get form data
            action = request.POST['follow_btns']
            # follow or unfollow
            if action == "unfollow":
                curr_user_profile.follows.remove(profile)
            elif action == "follow":
                curr_user_profile.follows.add(profile)
            # save profile
            curr_user_profile.save()

        return render(request, 'profile.html', {"currentuserprofile": currentuserprofile, "profile": profile, "projects": projects})
    else:
        # message.success(request, "You musst be logged in to view this page...")
        return redirect('home')


def myprojects(request):
    if request.user.is_authenticated:
        curr_user = request.user
        projects = Project.objects.filter(user=curr_user).order_by("-time_created")

        projectcreationform = ProjectCreationForm(request.POST or None)
        if request.method == 'POST':
            if projectcreationform.is_valid():
                project = projectcreationform.save(commit=False)
                project.user = request.user
                project.save()
                # messages.success(request, ("Your project has been saved!"))

                return redirect('myprojects')

        return render(request, 'myprojects.html', {"projects": projects, "projectcreationform": projectcreationform})
    else:
        return render(request, 'myprojects.html')


def project(request, projkey):
    if request.user.is_authenticated:
        proj = Project.objects.filter(id=projkey)
        materials = ProjectMaterial.objects.filter(project=proj[0])
        return render(request, 'project.html', {"project": proj[0], "materials": materials})
    else:
        return redirect('home')


def explore(request):
    projects = Project.objects.filter(visibility="PUBLIC")
    if request.user.is_authenticated:
        user = request.user
        return render(request, 'explore.html', {"user": user, "projects": projects})

    else:
        return render(request, 'explore.html', {"projects": projects})