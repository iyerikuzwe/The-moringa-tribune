from django.http  import HttpResponse
from django.shortcuts import render
from .models import Image

def home(request):
    """
    Function that renders the landing page
    """
    images = Image.get_images()
    return render(request, 'home.html', {"images":images})

def search_image(request):
    """
    Function that searches images by category
    """
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_image(category)
        message = f"{category}"
        
        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message":message})


def filter_by_location(request,location_id):
    """
    Function that filters images by location
    """
    images = Image.filter_by_location(id= location_id)
    return render (request, 'location.html', {"images":images})

7