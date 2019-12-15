SERVER ={
    'url': 'https://restcountries.eu/rest/v2/'
}

FULL_ROUTE = '{url}'.format(**SERVER)


if __name__ == '__main__':
    print(FULL_ROUTE)


'''

https://restcountries.eu/rest/v2/

praca domowa… korzystając z tego api, tworzymy pliki tekstowe o nazwie identycznej z trzyliterową nazwą waluty a w nim lista państw posługujących się tą walutą.
oczywiście piszemy aplikację w pythonie

'''