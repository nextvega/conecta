from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'home/feed.html',{
        'title': 'Feed'
    })

def user(request):
    return render(request, 'user/user.html',{
        'title': 'User'
    })