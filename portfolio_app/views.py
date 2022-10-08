from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'portfolio_base/index.html', {'t': [1, 2], 'm': [1, 2, 3], 'n': [1, 2, 3, 4]})


# def index(request):
#     return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def basic_data(request):
    return render(request, 'basic_info.html')


def certificates(request):
    return render(request, 'certificates.html')


def skills(request):
    return render(request, 'skills.html')


def education(request):
    return render(request, 'education.html')


def work_experience(request):
    return render(request, 'work_experience.html')


def social_media(request):
    return render(request, 'social_media.html')


# Create your views here.
def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'image_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
