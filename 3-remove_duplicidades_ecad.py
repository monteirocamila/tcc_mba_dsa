# Algoritmo para gerar arquivo com os nomes das músicas e compositores sem duplicidade,
# a partir do arquivo de origem que contém as informações sobre o ranking ECAD.

# Define diretório dos arquivos
dir = 'datasets/nome_musicas_ecad'

# Abre o arquivo de origem para leitura
arquivo_origem = open("datasets/ranking_ecad.txt", "r")

# Cria nova lista para receber as linhas do arquivo de origem
lista_temp = []

# Adiciona somente os campos de interesse do arquivo de origem a lista temporária
for li in arquivo_origem:
    linha = li.replace("\n", "").split(",")
    nova_linha = ','.join([str(v) for v in linha[4:6]])
    lista_temp.append(nova_linha)

# Cria uma nova lista sem linhas duplicadas
lista_unica = list(set(lista_temp))

# Cria arquivo destino
arquivo_destino = open("datasets/musicas_ecad_sem_duplicidade.txt", "w", encoding="utf-8")

# Escreve os itens da lista no arquivo destino
for item in lista_unica:
    arquivo_destino.write(item + "\n")
