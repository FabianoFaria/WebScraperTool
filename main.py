from bs4 import BeautifulSoup

with open('../OkamiWeb/index.html', 'r') as html_file:
    
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')

    """ Encontra apenas o primeiro elemento"""
    tags = soup.find('h5') 

    """ Encontra todos os elementos """

    all_tags = soup.find_all('h5') 

    print(all_tags)
