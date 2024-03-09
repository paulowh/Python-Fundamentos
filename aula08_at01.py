from bs4 import BeautifulSoup
import requests
import openpyxl

def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook() # -> cria a estancia do excel
        planilha = excel.active # -> pega a primeira planilha disponivel

        for linha in dados:
            planilha.append(linha)
        excel.save(nome_arquivo + '.xlsx')
        print('Dados salvos com sucesso no arquivo {}.xlsx'.format(nome_arquivo))
    except Exception as ex:
        print('Ocorreu um erro: {}'.format(ex))


url =  'https://paulowh.com'

resposta = requests.get(url)

if resposta.status_code == 200:
    #analisa o conteudo em html
    soup = BeautifulSoup(resposta.text, 'html.parser')

    section = soup.find('section', id='experience')
    dados = []
    for row in section.find_all('div', class_='card-content'):
        cargo = row.find('h6', class_='timeline-title').text.strip()
        empresa = row.find('h6', class_='empresa').text.strip()
        periodo = row.find('h6', class_='periodo').text.strip()
        desc = row.find('p').text.strip()
        dados.append([
            empresa,
            cargo, 
            periodo, 
            desc
        ])



GravarArquivoXLSX(dados, 'ex_paulin')