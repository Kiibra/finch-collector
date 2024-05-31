from django.shortcuts import render, redirect
# import the finch model
from .models import Finch, Toy
# Add import to use the class view
# Add UpdateView & DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import the FeedingForm
from .forms import FeedingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Define the home view
# convert existing home view function to a CBV that inherits from the LoginView class
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

# Add new view
def finch_index(request):
  # finches = Finch.objects.all() #this gets everyone's finches 
  # could retrieve so the logged user only see their finches 
  finches = Finch.objects.filter(user=request.user)
  return render(request, 'finches/index.html', { 'finches': finches })

# update this view function adding the new FeedingsForm
def finch_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
    # Get the toys the finch doesn't have
  toys_finch_doesnt_have = Toy.objects.exclude(id__in = finch.toys.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'finches/detail.html', {
    # include the finch and feeding_form in the context
    # Add the toys to be displayed
    'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have
  })

class FinchCreate(CreateView):
  model = Finch
  # fields = '__all__'
  #update fields so we can selectively show the fields we want. instead of all
  fields = ['name', 'breed', 'description', 'age']
  # valid finch form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the finch
    # CreateView validate the form
    return super().form_valid(form)

class FinchUpdate(UpdateView):
  model = Finch
  # disallow the renaming of a finch by excluding the name field!
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches/'

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('finch-detail', finch_id=finch_id)

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, finch_id, toy_id):
  # Note, can pass a toy's id instead of the whole object
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('finch-detail', finch_id=finch_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This creates a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This will log a user in
      login(request, user)
      return redirect('finch-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})