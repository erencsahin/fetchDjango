from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from images.models import Image, User
from utils.azure_blob import AzureBlobService
import uuid
from django.contrib.auth.hashers import make_password, check_password

def fetch_images_api(request, query):
    api_url = f"https://api.pexels.com/v1/search?query={query}"
    headers = {
        "Authorization": settings.MY_API_KEY
    }
    try:
        response = request.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        azure_service = AzureBlobService()

        for photo in data['photos']:
            image_url = photo['src']['original']
            photographer = photo['photographer']

            image_data = request.get(image_url).content
            unique_id = uuid.uuid4()
            blob_name = f"{photographer}/{unique_id}.jpg"
            blob_url = azure_service.upload_data(image_data, blob_name)

            photo['url'] = blob_url
            photo['src']['original'] = blob_url

            Image(title=photographer, url=blob_url).save()

        return JsonResponse({"data": data})
    except request.RequestException as e:
        return JsonResponse({"error": str(e)}, status=400)

def home(request):
    images = Image.objects.all()
    total_images = images.count()
    context = {
        'total_images': total_images,
        'images': images,
    }
    return render(request, 'home.html', context)

def show_images(request):
    mongo_client = mongo_client('localhost', 27017)
    db = mongo_client.mytextdb
    collection = db['images_image']

    images_cursor = collection.find()
    images = list(images_cursor)

    context = {
        'images': images,
    }
    return render(request, 'show-images.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(response)

        user = User.objects(username=username).first()
        if user and check_password(password, user.password):
            
            return HttpResponse("Login successful")
            
        return HttpResponse("Invalid credentials")
    return render(request, 'login.html')


def register_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if User.objects(username=username).first():
            return HttpResponse('böyle bir kullanici var')
        
        hashed_password=make_password(password)
        user=User(username=username, password=hashed_password)
        user.save();
        return HttpResponse('user registered successfully.')
    return render(request, 'register.html')