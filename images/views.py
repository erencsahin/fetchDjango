from django.shortcuts import render
from .models import Image

# Create your views here.

import requests
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
    except requests.RequestException as e:
        return render(request,'home.html',{'error':str(e)})
    
    

    for photo in data['photos']:
        Image.objects.create(
            title=photo['photographer'],
            url=photo['src']['original']
        )


def home(request):
    images = Image.objects.all()
    total_images = images.count()
    context = {
        'total_images': total_images,
        'images': images,
    }
    return render(request, 'home.html', context)


