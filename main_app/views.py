from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'tabby', 'Kinda rude.', 3),
  Finch('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Finch('Fancy', 'bombay', 'Happy little ball.', 4),
  Finch('Bonk', 'selkirk rex', 'Chirps loudly.', 2),
  Finch('Leila', 'selkirk rex', 'Chirps loudly.', 0),
  Finch('Bnk', 'selkirk rex', 'Chirps loudly.', 5),
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Finches🦜</h1>')

def about(request):
  return render(request, 'about.html')

# Add new view
def finch_index(request):
  return render(request, 'finches/index.html', { 'finches': finches })