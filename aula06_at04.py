caminho_arquivo = 'categorias.csv'
categorias = open(caminho_arquivo, 'r', encoding='utf-8')

lista_categoria = [] #-> chaves

for linha in categorias:
    colunas = linha.strip().split(';')
    lista_categoria.append([colunas[2] == colunas[0]])

print(lista_categoria)
