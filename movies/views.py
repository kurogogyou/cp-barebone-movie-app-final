from django.shortcuts import render, redirect
from django.contrib import messages
from airtable import Airtable
import os

# Create your views here.

# https://www.genesisglobalschool.edu.in/wp-content/uploads/2016/09/noimage.jpg

# Airtable database handler
AT = Airtable(os.environ.get('AIRTABLE_MOVIESTABLE_BASE_ID'), 'Movies', api_key=os.environ.get('AIRTABLE_API_KEY'))

# This runs when soembody comes to my website
def home_page(request):

	# Searches based on the text query. Case insensitive (converts to lowercase).
	user_query = str(request.GET.get('query', ''))
	search_result = AT.get_all(formula="FIND('" + user_query.lower() + "', LOWER({NAME}))")
	stuff_for_frontend = {'search_result': search_result}

	return render(request, 'movies/movies_stuff.html', stuff_for_frontend)

def create(request):
	if request.method == 'POST':
		try:
			data = {
				'Name': request.POST.get('name'),
				# Add default No Image picture if none was provided.
				'Pictures' : [{'url' : request.POST.get('url') or 'https://www.genesisglobalschool.edu.in/wp-content/uploads/2016/09/noimage.jpg'}],
				'Rating': int(request.POST.get('rating')),
				'Notes': request.POST.get('notes')
			}
			
			response = AT.insert(data)
			#response['fields'] is a dictionary too.
			messages.success(request, 'New movie added: {}'.format(response['fields'].get('Name')))
		except Exception as e:
			messages.warning(request, 'Error when creating: {}'.format(e))

	return redirect('/')

def edit(request, movie_id):
	if request.method == 'POST':
		try:
			data = {
				'Name' : request.POST.get('name'),
				'Pictures' : [{'url' : request.POST.get('url')}],
				'Rating' : int(request.POST.get('rating')),
				#'Notes' : request.POST.get('notes')
			}
			#Only update the notes when the string is not empty. Prevents automatically removing notes.
			if request.POST.get('notes') != '':
				data.update({'Notes' : request.POST.get('notes')})

		
			response = AT.update(movie_id, data)
			messages.success(request, 'Edited movie: {}'.format(response['fields'].get('Name')))
		except Exception as e:
			messages.warning(request, 'Error when updating: {}'.format(e))
	return redirect('/')

def delete(request, movie_id):
	try:
		#Need to get the name of the movie before I delete it.
		name = AT.get(movie_id)['fields'].get('Name')
		AT.delete(movie_id)
		messages.warning(request, 'Deleted movie: {}'.format(name))
	except Exception as e:
		messages.warning(request, 'Error when deleting: {}'.format(e))
	return redirect('/')