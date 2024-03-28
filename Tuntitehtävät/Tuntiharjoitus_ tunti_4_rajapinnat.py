# moduuli 12, rajapinnat

import requests


def search_shows(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"

    try:
        response = requests.get(url)


        print(f"HTTP response status code: {response.status_code}")
        shows = response.json()
        # print(f"ensimmäisen sarjan nimi {shows[0]['show']['name']}")
        # tulostetaan hakutulokset for loopilla, mikäli hakupyyntö on ok, eli koodi 200
        if response.status_code == 200:
            print(f"\nHaun tulokset hakusanalla {search_term}:")
            for show in shows:
                # haetaan genret sisäkkäisellä silmukalla
                genres = ""
                for genre in show['show']['genres']:
                    genres = genres + genre + " "
                print(f"Sarjan nimi {show['show']['name']}, genret: {genres}, {show['show']['url']}")
    except requests.exceptions.RequestException as error:
        print(f"HTTP pyyntö meni pieleen, ei verkkoyhteyttä palvelimeen")
        print(error)
    except Exception as error:
        print("HTTP-pyyntö meni pieleen")
        print(error)


search_input = input("Anna hakusana:\n>")
search_shows(search_input)