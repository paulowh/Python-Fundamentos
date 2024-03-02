'''
Atividade: Juntar as informações de duas planilhas (categorias e produtos)
    - abrir o primeiro arquivo CSV -> ok
    - guardar as infor do 1º arquivo CSV -> ok
    - abrir o segundo arquivo CSV -> ok
    - guardar as infor do 2º arquivo CSV -> ok
    - mesclar / tratar as informações com os ~valores correspondente~
    - manter somente as info nescessarias
    - converter as info para o xlsx 
'''
import openpyxl

def CarregarArquivoCSV(nome_arquivo):
    dados_arquivo = open(nome_arquivo + '.csv', 'r', encoding='utf-8')
    
    lista_info = [] #-> array vazio
    for linha in dados_arquivo:
        colunas = linha.strip().split(';')
        lista_info.append(colunas)

    return lista_info

def ConcatenarArquivosCSV(categoriasCSV, produtosCSV):
    dados_csv = []
    dados_csv.append([
        'id_produto',
        'nome_produto',
        'quantidade',
        'valor_venda',
        'valor_compra',
        'id_categoria',
        'nome_categoria'
    ])
    for produto in produtosCSV:
        index = int(produto[2]) - 1
        # dados_csv.append([*produto, *categoriasCSV[index]])

        dados_csv.append([
            produto[0],
            produto[1],
            produto[4],
            produto[8],
            produto[9],
            categoriasCSV[index][0],
            categoriasCSV[index][1] 
        ])

    return dados_csv

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


dados_categoria = CarregarArquivoCSV('categorias')
dados_produto = CarregarArquivoCSV('produtos')
dados_concatenados = ConcatenarArquivosCSV(dados_categoria, dados_produto)

GravarArquivoXLSX(dados_concatenados, 'info_tratadas')