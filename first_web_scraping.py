from bs4 import BeautifulSoup
import requests

url = "https://www.sinefil.com/liste/z29erwl"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
liste = soup.find('div', {'class': 'movie-container'}).find_all('div', {'class': 'col-lg-9'})
count = 0
for i in liste:
    nameTr = i.find('h3', {'class': 'hero'}).text.strip('0123456789()')
    nameEn = i.find('div', {'class': 'mini-hero'}).text.strip()
    point = i.find('ul', {'class': 'left'}).find_all('li')[1].text.replace('\n', ':').strip(':').replace('puanı',
                                                                                                         'Rating')

    info = i.find('table').find_all('td', {'class': 'text-right'})
    """
        info[0]=year
        info[1]=time
        info[2]=category
    """
    info[0] = info[0].text.replace('\n', ':').strip(': ')
    info[1] = info[1].text.replace('\n', ':').strip(': ').replace('Saat', 'hour').replace('Dk.', 'minutes')
    info[2] = info[2].text.replace('\n', ' , ').strip(' , ')
    count += 1

    print(
        f'{count}- Movie name:{nameEn.ljust(56)},Turkish movie name:{nameTr.ljust(44)}, {point.center(13)} , Vision date:{info[0].ljust(15)} , Duration : {info[1].ljust(20)} , Category:  {info[2]}')

