from config import FULL_ROUTE
import os
import io
import requests
import json
from json import JSONDecodeError

def request(method, path, post_data: dict=None):
    """
    Function downloads all dates from api and decode them
    :param method: 
    :param path: 
    :param post_data: 
    :return: 
    """""
    response = requests.request(
        method,
        url=f'{FULL_ROUTE}{path}',
        json=post_data,
        headers={
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'
            'Content-type": "application/json; charset=UTF-8'
        }
    )

    try:
        content = json.loads(response.content.decode())
    except JSONDecodeError:
        content = response.content.decode()

    return content

def country_currencies(all_countries):
    """
    Function extracts from content name of country and code of currency.
    Next creates dict which key is code of country and values are countries.
    :param all_countries: 
    :return: 
    """""
    dict_currency = {}
    for country in all_countries:
        country_name = country['name']
        for currency in country['currencies']:
            country_currency = currency['code']
            if country_currency != '(none)' and country_currency != None:
                if not country_currency in dict_currency:
                    dict_currency[country_currency] = [country_name]
                else:
                    dict_currency[country_currency] = dict_currency[country_currency] + [country_name]
    return dict_currency

def create_currency_files(dict_currencies_with_countries, target_path =''):
    """
    Function creates the files, which name is code of currency and content are countries.
    :param dict_currencies_with_countries:
    :param target_path:
    :return:
    """
    for currency in dict_currencies_with_countries:
        with open(f'{target_path}/{currency}.txt', 'w') as file:
            file.write('\n'.join(dict_currencies_with_countries[currency]))


if __name__ == '__main__':
    all_countries = request('GET', 'all')
    dict_currencies_with_countries = country_currencies(all_countries)
    create_currency_files(dict_currencies_with_countries, 'waluty')
