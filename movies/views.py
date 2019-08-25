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

	# Searches based on the text query. Case insensitive (converts to lowercase).
	user_query = str(request.GET.get('query', ''))
	search_result = AT.get_all(formula="FIND('" + user_query.lower() + "', LOWER({NAME}))")
	stuff_for_frontend = {'search_result': search_result}

	return render(request, 'movies/movies_stuff.html', stuff_for_frontend)


