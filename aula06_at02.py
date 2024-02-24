# . -> pasta atual
# .. -> retorno de pasta

caminho_arquivo = 'categorias.csv'

# r -> read -> leitura
# w -> write -> escrita
categorias = open(caminho_arquivo, 'r', encoding='utf-8')

lista_categoria = {} #-> chaves

for linha in categorias:
    colunas = linha.strip().split(';')
    # lista_categoria.append([colunas[0], colunas[1]])
    lista_categoria[colunas[0]] = [colunas[1], colunas[2]]

print(lista_categoria)