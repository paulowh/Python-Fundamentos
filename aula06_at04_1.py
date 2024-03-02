import openpyxl
'''
Atividade: Converter o arquivo csv em xlsx
    - identificar o nome do arquivo csv -> ok
    - abrir o arquivo -> ok
    - guardar as informações do arquivo -> ok
    - criar um novo arquivo xlsx (com o mesmo nome do arquivo csv)
    - inserir as informações guardadas no novo arquivo
'''

def CarregarArquivoCSV(nome_arquivo):
    dados_arquivo = open(nome_arquivo + '.csv', 'r', encoding='utf-8')
    
    lista_info = [] #-> array vazio
    for linha in dados_arquivo:
        colunas = linha.strip().split(';')
        lista_info.append(colunas)

    # soma = 0
    # for linha2 in lista_info:
    #     soma = soma + int(linha2[0])
    #     print(soma)
        
    return lista_info

def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook() # -> cria a estancia do excel
        planilha = excel.active # -> pega a primeira planilha disponivel

        for linha in dados:
            planilha.append(linha)
        excel.save(nome_arquivo + '.xlsx')
        print('Dados salvo com sucesso no arquivo {}.xlsx'.format(nome_arquivo))
    except Exception as ex:
        print('Ocorreu um erro: {}'.format(ex))

# nome_arquivo = input('Informe o nome do arquivo (sem a extensão): ')
nome_arquivo = 'categorias'
dados_csv = CarregarArquivoCSV(nome_arquivo)
GravarArquivoXLSX(dados_csv, nome_arquivo)