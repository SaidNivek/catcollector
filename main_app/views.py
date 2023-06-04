from django.shortcuts import render
# Import the CreateView generic class so we can use it
from django.views.generic.edit import CreateView
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

# We are using the CreateView generic class and are using it to extend the class
class CatCreate(CreateView):
  model = Cat
  # fields is required for a CreateView and can be used to limit or change the ordering of the attrivutes fromt he Cat model when generated in the ModelForm and passed to the template
  # __all__ will select all of the fields from the Cat model, but you can write them out as such:
  # fields = ['name', 'breed', 'description', 'age']
  fields = '__all__'



# Add this cats list below the imports
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]