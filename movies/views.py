from django.shortcuts import render
from django.contrib import messages
#from airtable import airtable
import os

# Create your views here.

def home_page(request):
	return render(request, 'movies/movies_stuff.html')

# This runs when soembody comes to my website
