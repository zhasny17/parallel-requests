import requests
import os

session = requests.Session()

URLS = [f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png' for number in range(1, 151)]

def main():
    for url in URLS:
        try:
            response = session.get(url)
            if response.ok:
                if not os.path.exists('images/sequence_alg/'):
                    os.makedirs('images/sequence_alg/')
                image_name = url.split('pokemon/')[1]
                with open(f'images/sequence_alg/{image_name}', 'wb') as f:
                    f.write(response.content)
        except requests.exceptions.ConnectionError as err:
            pass


if __name__ == '__main__':
    main()