from django.shortcuts import render
# Import the Cat Model
from .models import Cat

# Create your views here:

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

# About the app / and me
def about(request):
  return render(request, 'about.html')

# Index of all cats
def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })

# Detail page for a clicked cat
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })


# Add this cats list below the imports
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]