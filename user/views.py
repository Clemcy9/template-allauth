from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    print(f' default user model is {User}')
    return render(request, 'index.html')