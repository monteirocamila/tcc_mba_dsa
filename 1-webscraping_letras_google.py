# Algoritmo para gerar um arquivo texto com as letras das músicas presentes no arquivo
# de origem, através de webscraping no site do Google.

# Importação de pacotes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Define diretorios e nome de arquivos
origem = "datasets/musicas_playlists.csv"

# Cria arquivo destino em branco
destino = "datasets/playlists_letras_recuperadas_google.txt"
open(destino, "w", encoding="utf-8")

# Abre o arquivo de origem para leitura
arquivo_origem = open(origem, "r", encoding="utf-8")

# Realiza a leitura do arquivo de origem
for li in arquivo_origem:

    # Recupera e trata o nome da musica
    linha = li.replace("\n", "").split(",")
    filtro_full = linha[0] + " " + linha[1] + " letra"

    # Define resolução navegador
    opt = Options()
    opt.add_argument("window-size=400,800")
    # Define configurações para acesso a url
    nav = webdriver.Chrome(options=opt)
    # Abre conexão com o site
    nav.get("https://www.google.com.br")
    nav.find_element_by_name("q").send_keys(filtro_full)
    nav.find_element_by_name("q").send_keys(Keys.RETURN)

    # Abre arquivo destino para edição
    arquivo_destino = open(destino, "a", encoding="utf-8")

    try:
        # Recupera o conteúdo na página web e realiza tratamentos para limpeza de dados
        lista_letra = nav.find_element_by_class_name("xaAUmb").text.split('\n')
        letra = ' '.join([str(x) for x in lista_letra])
        letra_tratada = letra.replace(",", "")
        linha.append(letra_tratada)
        # Armazena o conteúdo encontrado no arquivo
        arquivo_destino.write(', '.join([str(x) for x in linha]) + "\n")
    except:
        # Armazena mensagem de conteúdo não encontrado no arquivo
        linha.append("Letra não encontrada")
        arquivo_destino.write(', '.join([str(x) for x in linha]) + "\n")
    # Encerra conexão
    nav.close()
