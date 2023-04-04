# Algoritmo para gerar um arquivo texto com as letras das músicas presentes no arquivo
# de origem referente as músicas das playlists, através de webscraping no site do Google.

# Importação de pacotespd.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Lê o arquivo de origem, remove duplicidades e gera um novo arquivo.
arq_origem = pd.read_csv('datasets/ranking_billboard.csv')
arq_origem = arq_origem.drop_duplicates()
arq_origem = arq_origem.drop(columns=['ranking','c1','c2','c3'])
arq_origem.to_csv('datasets/ranking_billboard_tratado.csv',encoding="utf-8")
#print(arq_origem.head())

# Remove a data do dataframe e remove as duplicidades para manter somente uma ocorrencia para cada música
base_musicas = arq_origem.drop(columns=['data'])
base_musicas = base_musicas.drop_duplicates()
base_musicas.to_csv('datasets/base_musicas_billboard_sem_dup.csv',encoding="utf-8")
#print(base_musicas)

# Varre o dataframe realizar a recuperação das letras de música
for index, linha in base_musicas.iterrows():
    # Define filtro para pesquisa
    filtro_full = linha["musica"] + " " + linha["interprete"] + " letra"
    filtro = linha["musica"] + " letra"
    # Define resolução navegador
    opt = Options()
    opt.add_argument("window-size=400,800")
    # Define configurações para acesso a url
    nav = webdriver.Chrome(options=opt)
    # Abre conexão com o site
    nav.get("https://www.google.com.br")
    # Envia condição para pesquisa
    nav.find_element_by_name("q").send_keys(filtro_full)
    # Retorna resultado da pesquisa
    nav.find_element_by_name("q").send_keys(Keys.RETURN)
    try:
        # Recupera o conteúdo na página web e realiza tratamentos para limpeza de dados
        lista_letra = nav.find_element_by_class_name("xaAUmb").text.split('\n')
        letra = ' '.join([str(x) for x in lista_letra])
        letra_tratada = letra.replace(",", "")
        # Armazena o conteúdo encontrado no dataframe
        base_musicas.loc[index, "letra"] = letra_tratada
    except:
        try:
            # Encerra conexão
            nav.close()
            # Define configurações para acesso a url
            nav = webdriver.Chrome(options=opt)
            # Abre conexão com o site
            nav.get("https://www.google.com.br")
            # Envia condição para pesquisa
            nav.find_element_by_name("q").send_keys(filtro)
            # Retorna resultado da pesquisa
            nav.find_element_by_name("q").send_keys(Keys.RETURN)
            # Recupera o conteúdo na página web e realiza tratamentos para limpeza de dados
            lista_letra = nav.find_element_by_class_name("xaAUmb").text.split('\n')
            letra = ' '.join([str(x) for x in lista_letra])
            letra_tratada = letra.replace(",", "")
            # Armazena o conteúdo encontrado no dataframe
            base_musicas.loc[index, "letra"] = letra_tratada
        except:
            # Armazena mensagem de conteúdo não encontrado no arquivo
            base_musicas.loc[index, "letra"] ="Letra não encontrada"
    # Encerra conexão
    nav.close()
# Gera arquivo com a base final
base_musicas.to_csv('datasets/ranking_billboard_letras_musicas.csv', sep=',', index = False, encoding='utf-8')