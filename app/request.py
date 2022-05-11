import urllib.request, json
from .main import main
from .models import Pet, Movie

# get api key
# api_key = app.config['PET_API_KEY']
# api_key ='XR1OHuhS8M02Twf4ZtcWVv7qXNOOTEoD1b5q8C0ZTD127lfQqE'
# api_secret = 'N91wgDJWoM0lXmJpbhIAR51EF1cts9Dp0vCjdmUq'
# base_url = 'https://api.petfinder.com/v2/animals'

base_url = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
api_key = '91c09537ef238ac29bc0f1d2989ec7f9'
category = "popular"


# def get_petlist_token():
#     request = f'{base_url}/grant_type=client_credentials&client_id={api_key}&client_secret={api_secret}'
#     re
    
    
# get base url
# base_url = app.config["PET_API_BASE_URL"]
# headers = {
#      "Authorization": f"Bearer {token}"
# }

def fetch_pets():
    # fetch from api
    pets_url = base_url.format(category,api_key)
    with urllib.request.urlopen(pets_url) as url:
        get_pet_data = url.read()
        get_pet_response = json.loads(get_pet_data)
        
        pet_list = None
        
        if get_pet_response:
            pet_result_list = get_pet_response['results']
            petlist = process_results(pet_result_list)

    return petlist

def process_results(pet_list):
    '''
    Function  that processes the pet result and transform them to a list of Objects

    Args:
        pet_list: A list of dictionaries that contain movie details

    Returns :
        pet_results: A list of pet objects
    '''
    pet_results = []
    for pet in pet_list:
        id = pet.get('id')
        title = pet.get('original_title')
        overview = pet.get('overview')
        poster = pet.get('poster_path')
        vote_average = pet.get('vote_average')
        vote_count = pet.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            pet_results.append(movie_object)

    return pet_results


def search_pets(movie_name):
    search_movie_url = 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)


    return search_movie_results