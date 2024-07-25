from django.shortcuts import render,redirect
from .models import Image
from pymongo import MongoClient
from utils.fetch_data_upload_blob import fetch_data_upload_blob

# Create your views here.

import requests
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import render


def fetch_images(request, query):
    url = f"https://api.pexels.com/v1/search?query={query}"
    headers = {
        "Authorization": settings.MY_API_KEY
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        for photo in data['photos']:
            Image.objects.create(
                title=photo['photographer'],
                url=photo['src']['original']
            )
        
        return JsonResponse(data)
    except requests.RequestException as e:
        return render(request, 'home.html', {'error': str(e)})

def home(request):
    images = Image.objects.all()
    total_images = images.count()
    context = {
        'total_images': total_images,
        'images': images,
    }
    return render(request, 'home.html', context)


def show_images(request):
    mongo_client = MongoClient(
        settings.DATABASES['default']['CLIENT']['host'],
        settings.DATABASES['default']['CLIENT']['port']
    )
    db = mongo_client[settings.DATABASES['default']['NAME']]
    collection = db['images_image']

    images_cursor = collection.find()
    images = list(images_cursor)

    context = {
        'images': images,
    }
    return render(request, 'show-images.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login credentials")
    return render(request, 'login.html')


def upload_data_to_blob(request):
    api_url=''
    blob_name=''

    try:
        fetch_data_upload_blob(api_url,blob_name)
        return HttpResponse('data fetched and uploaded to blob')
    except Exception as e:
        return HttpResponse(f'an error occured: {str(e)}',status=500)