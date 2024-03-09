from bs4 import BeautifulSoup
import requests

def ConsultaSitePagueMenos(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        page = soup.find('div', class_='list-products page-content')

        prod_paguemenos = []
        for row in page.find_all('div', class_='desc position-relative'):
            produto = row.find('h2').text.strip()
            preco = row.find('p', class_='sale-price').text.strip()
            
            prod_paguemenos.append([
                produto, 
                preco
            ])
        
        return prod_paguemenos

def ConsultaSiteSaoVicente(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')

        page = soup.find('body')
        print(page)
        # for row in page.find_all('div', 'ng-star-inserted'):
        #     print(row)

url =  'https://www.superpaguemenos.com.br/hortifruti/'

ConsultaSitePagueMenos(url)
ConsultaSiteSaoVicente('https://www.paranasupermercadoonline.com.br/produtos/departamento/hortifruti/fruta')