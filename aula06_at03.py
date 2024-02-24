import openpyxl

def criar_planilha(arquivo, dados):
    try:
        excel = openpyxl.Workbook() # -> criando o excel

        planilha = excel.active # -> a primeira aba ativa


        for linha in dados:
            planilha.append(linha) # -> adicionar mais infomações

        excel.save(arquivo)

        print('Dados salvo com sucesso no arquivo {}'.format(arquivo))

    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))



arquivo_excel = 'minhas_series.xlsx'

dados = [
    ['Doctor Who', '1960'],
    ['o gambito da rainha', '2022'],
    ['Mr. Robot', '2015'],
    ['o gambito da rainha', '2022'],
    ['Mr. Robot', '2015'],
    ['o gambito da rainha', '2022'],
    ['Mr. Robot', '2015'],
    ['o gambito da rainha', '2022'],
    ['Mr. Robot', '2015'],
    ['As tranças do rei careca', '1900']
]

criar_planilha(arquivo_excel,dados)