
# Importação de pacotes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from datetime import date, timedelta

# Define configurações do navegador
opt = Options()
opt.add_argument("window-size=400,800")

# Cria arquivo em branco
arquivo = open("datasets/ranking_billboard.csv", "w", encoding="utf-8")
# Cria cabeçalho
arquivo.write("ranking,musica,interprete,c1,c2,c3,data" + "\n")

# Define as datas de inicio e fim para os períodos que devem ser recuperados do site.
# O ranking Bilboard é semanal e a semana é indicada pela data do sábado e só possui dados do último ano
data_ref = datetime.datetime.strptime("2022/01/01","%Y/%m/%d").date() # Data de início
data_fim = datetime.datetime.strptime("2023/04/01","%Y/%m/%d").date() # Data de fim
dias = timedelta(7)

# Recupera as informações do ranking para o período definido
while data_ref <= data_fim:
    # Define o endereço do site
    endereco = "https://www.billboard.com/charts/brazil-songs-hotw/" + str(data_ref)
    # Abre conexão com o site
    nav = webdriver.Chrome(options=opt)
    nav.get(endereco)
    # Recupera o conteúdo do ranking
    itens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    palavras_out = ['NEW', 'RE- ENTRY']
    for item in itens:
        # Recupera o conteúdo de cada item do ranking da semana
        item_ranking = nav.find_elements_by_class_name('o-chart-results-list-row-container').__getitem__(item).text
        item_ranking = item_ranking.replace(",","/")
        conteudo_ranking = item_ranking.split('\n')
        # Recupera e trata a data de referência do ranking
        semana = nav.find_element_by_xpath("/html/body/div[4]/main/div[2]/div[3]/div/div/div/div[1]/p").text
        semana_replace = semana.replace("WEEK OF ","")
        data_ref_semana = datetime.datetime.strptime(semana_replace,"%B %d, %Y").date()
        conteudo_ranking.append(str(data_ref_semana))
        linha = ','.join([str(v) for v in conteudo_ranking if v not in palavras_out])
        # print(linha)
        # Armazena o conteúdo no arquivo
        with open("datasets/ranking_billboard.csv", "a",encoding="utf-8") as arquivo:
            arquivo.write(linha + "\n")
    # Encerra conexão
    nav.close()
    # Atualiza a data de referência
    data_ref = data_ref + dias







