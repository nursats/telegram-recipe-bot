import requests
from pprint import pprint

from bot.config import EDAMAM_APP_ID, EDAMAM_APP_KEY
def recipe():
    try: 
        url = 'https://api.edamam.com/api/recipes/v2'
        query = 'random'
        params = {
        'q': query,
        'app_id': EDAMAM_APP_ID,
        'app_key': EDAMAM_APP_KEY,
        'type': 'public'
        }
        r = requests.get(url, params=params)
        data = r.json()
        pprint(data)

    except Exception as ex:
        print(ex)
        print('there was problem') 



def main():
    city = input("Your city: ")
    recipe()

if __name__ == '__main__':
    main()