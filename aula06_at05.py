from os import system
import openpyxl

def CarregarArquivoCSV(nome_arquivo):
    caminho_arquivo = nome_arquivo + '.csv'
    categorias = open(caminho_arquivo, 'r', encoding='utf-8')

    lista_categoria = [] # -> com a abertura do cochetes temos um array vazio

    for linha in categorias:
        colunas = linha.strip().split(';')
        lista_categoria.append(colunas)

    return lista_categoria

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

def ConcatenarArquivosCSV(categoriaCSV, produtosCSV):

    dados = []    
    for produto in produtosCSV:
        dados.append([*produto, *categoriaCSV[ int(produto[2]) - 1 ]])

    return dados


system('cls')
#nome_arquivo = input('Digite o nome do arquivo: (sem as extensão) ')

categoriasCSV = CarregarArquivoCSV('categorias') # -> consultamos o arquivo
produtosCSV = CarregarArquivoCSV('produtos') # -> consultamos o arquivo
dadosConcatenados = ConcatenarArquivosCSV(categoriasCSV, produtosCSV)
GravarArquivoXLSX(dadosConcatenados, 'nome_arquivo') # -> passamos o resultado da ultima consulta e gravamos no novo tipo de arquiv
