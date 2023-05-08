import requests
from HW_1 import logger

def get_all_superheroes_list (url='https://akabab.github.io/superhero-api/api/all.json'):
    superheroes_list = requests.get(url)
    return superheroes_list.json()

@logger
def smartest_superhero(list_heroes):
    all_superheroes = get_all_superheroes_list()
    max_intelligence = 0
    smartest_hero = []
    for name in list_heroes:
        for superhero in all_superheroes:
            if superhero['name'] == name:
                intelligence = superhero['powerstats']['intelligence']
                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    smartest_hero = [name]
                elif intelligence == max_intelligence:
                    max_intelligence = intelligence
                    smartest_hero.append(name)
    return print(smartest_hero)

def main():
    superheros = ['Hulk', 'Captain America', 'Thanos', 'Iron man', 'Vision']
    smartest_superhero(superheros)
    # get_name_intelligence_list()

if __name__ == '__main__':
    main()