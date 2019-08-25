from django.shortcuts import render
from django.contrib import messages
from airtable import Airtable
import os

# Create your views here.

# Airtable database handler
AT = Airtable(os.environ.get('AIRTABLE_MOVIESTABLE_BASE_ID'), 'Movies', api_key=os.environ.get('AIRTABLE_API_KEY'))

# This runs when soembody comes to my website
def home_page(request):
	#print(os.environ.get('AIRTABLE_API_KEY'))
	#print(os.environ.get('AIRTABLE_MOVIESTABLE_BASE_ID'))
	#print(str(request.GET.get('query', '')))
	user_query = str(request.GET.get('query', ''))
	return render(request, 'movies/movies_stuff.html')


