from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html',{
        'title': 'Login'
    })

def inicio(request):
    return render(request, 'home/home.html',{
        'title': 'Feed'
    })

def user(request):
    return render(request, 'user/user.html',{
        'title': 'User'
    })

def network(request):
    return render(request, 'network/network.html',{
        'title': 'Network'
    })

def jobs(request):
    return render(request, 'jobs/jobs.html',{
        'title': 'Jobs'
    })