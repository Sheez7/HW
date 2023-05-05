import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json

url = 'https://hh.ru/search/vacancy?text=python&area=1&area=2'
headers = {'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36', 'Accept-Language': 'en-US;q=0.5,en;q=0.3', 'Cache-Control': 'max-age=0', 'Upgrade-Insecure-Requests': '1'}
html = requests.get(url=url, headers=headers).text

soup = BeautifulSoup(html, features='lxml')
all_vacancies = soup.find(id='a11y-main-content')
vacancy = all_vacancies.find_all(class_='serp-item') 

description_list = [] 
for item in vacancy: 
    description_vacancy = item.find(class_='vacancy-serp-item__layout') 
    description = description_vacancy.find('a', class_='serp-item__title').text 
    if 'Django' in description or 'Flask' in description: 
        description_list.append(item) 

vacancy_list = [] 
for word in description_list: 
    title = word.find('a', class_='serp-item__title').text 
    link_tag = word.find('a', class_='serp-item__title')
    link = link_tag['href']
    try: 
        salary_tag = word.find('span', class_='bloko-header-section-3')
        salary = salary_tag.text
    except Exception: 
        salary = 'Не указана'
    company_tag = word.find('a', class_='bloko-link bloko-link_kind-tertiary') 
    company = company_tag.text 
    city_tag = word.find('div', attrs={'data-qa': 'vacancy-serp__vacancy-address', 'class': 'bloko-text'}) 

    vacancy_list.append({

        'Название': title,
        'Зарплата': salary,
        'Компания': company,
        'Город': city,
        'Ссылка': link

    }) 

with open('vacancy.json', 'w', encoding='utf=8') as f: 
    json.dump(vacancy_list, f, ensure_ascii=False)

if __name__ == '__main__':
    pprint(vacancy_list)
    