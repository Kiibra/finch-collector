from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello Finches🦜</h1>')

def about(request):
  return HttpResponse('<h1>About the FinchCollector🦜</h1>')