import datetime
from urllib import response
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def collect_data(city_code='2398'):
    cur_time = datetime.datetime.now().strftime('%d_%m_%Y_%H')
    uz = UserAgent()

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': uz.random
    }

    cookies = {
        'mg_geo_id': f'{city_code}'
    }

    
    response = requests.get(url='https://asaxiy.uz/product/telefony-i-gadzhety', headers=headers, cookies=cookies)

    

    with open(f'index.html', 'w', encoding="utf-8") as file:
        file.write(response.text)

def main():
    collect_data(city_code='2398')

if __name__ == '__main__':
    main()