from django.shortcuts import render, redirect
# Import the generic classes so we can use them
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the Cat Model
from .models import Cat
# Import the FeedingForm
from .forms import FeedingForm

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
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form
  })

def add_feeding(request, cat_id):
 # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.cat_id = cat_id
    new_feeding.save()
  return redirect('detail', cat_id=cat_id)

# We are using the CreateView generic class and are using it to extend the class
class CatCreate(CreateView):
  model = Cat
  # fields is required for a CreateView and can be used to limit or change the ordering of the attrivutes fromt he Cat model when generated in the ModelForm and passed to the template
  # __all__ will select all of the fields from the Cat model, but you can write them out as such:
  # fields = ['name', 'breed', 'description', 'age']
  fields = '__all__'

class CatUpdate(UpdateView):
  model = Cat
  # Disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'


# Add this cats list below the imports
cats = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]