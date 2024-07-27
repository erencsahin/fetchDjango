from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import requests
from pymongo import MongoClient
from images.models import Image
from utils.azure_blob import AzureBlobService
import uuid

def fetch_images(request, query):
    api_url = f"https://api.pexels.com/v1/search?query={query}"
    headers = {
        "Authorization": settings.MY_API_KEY
    }
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        azure_service = AzureBlobService()

        # Pexels API'den gelen fotoğrafların URL'lerini Azure Blob Storage URL'leri ile değiştirme
        for photo in data['photos']:
            image_url = photo['src']['original']
            photographer = photo['photographer']

            # Fotoğrafı indir ve Azure Blob Storage'a yükle
            image_data = requests.get(image_url).content
            unique_id = uuid.uuid4()
            blob_name = f"{photographer}/{unique_id}.jpg"
            blob_url = azure_service.upload_data(image_data, blob_name)

            # Fotoğraf URL'sini Azure Blob Storage URL'si ile güncelle
            photo['url'] = blob_url  # Pexels URL'sini Blob URL ile değiştir
            photo['src']['original'] = blob_url
            photo['src']['large2x'] = blob_url
            photo['src']['large'] = blob_url
            photo['src']['medium'] = blob_url
            photo['src']['small'] = blob_url
            photo['src']['portrait'] = blob_url
            photo['src']['landscape'] = blob_url
            photo['src']['tiny'] = blob_url

            # Blob URL'sini MongoDB'ye kaydet
            Image(title=photographer, url=blob_url).save()

        return JsonResponse({"data": data})
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
    mongo_client = MongoClient('localhost', 27017)
    db = mongo_client.mytextdb
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
