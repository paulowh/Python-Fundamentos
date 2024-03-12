import openpyxl
import requests
from bs4 import BeautifulSoup

# URL do site com a tabela
url = 'https://paulowh.com'
def ConsultaSite(url):
    # Fazendo a solicitação HTTP
    response = requests.get(url)

    if response.status_code == 200:
        # Analisando o conteúdo HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrando a tabela
        tag = soup.find('section', id='experience')
        
        # Iterando sobre as linhas da tabela
        row_data = []
        for row in tag.find_all('div', class_='card-content'):
            cargo  = row.find_all('h6', class_='timeline-title')
            empresa = row.find_all('h6', class_='empresa')
            periodo = row.find_all('h6', class_='periodo')
            desc    = row.find_all('p')

            row_data.append([
                cargo[0].text.strip() ,
                empresa[0].text.strip() ,
                periodo[0].text.strip() ,
                desc[0].text.strip()
            ])

            # print(row_data, '\n')
        return row_data
    else:
        print('Falha ao carregar a página:', response.status_code)

def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook() # -> criando o excel
        planilha = excel.active # -> a primeira aba ativa

        for linha in dados:
            planilha.append(linha) # -> adicionar mais infomações
        excel.save(nome_arquivo + '.xlsx') # -> fecho a conexão e dou o nome para o arquivo

        print('Dados salvo com sucesso no arquivo {}'.format(nome_arquivo))

    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))


dados = ConsultaSite(url)
GravarArquivoXLSX(dados, 'paulowh')

