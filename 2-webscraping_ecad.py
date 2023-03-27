# Algoritmo para gerar um arquivo texto com o ranking de músicas mais tocadas nas rádios brasileiras,
# através de webscraping no site do ECAD.

# Importação de pacotes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Define resolução navegador
opt = Options()
opt.add_argument("window-size=400,800")

# Abre conexão com o site
nav = webdriver.Chrome(options=opt)
nav.get("https://www4.ecad.org.br/ranking/")
sleep(1)

# Seleciona filtro de segmento
nav.find_element_by_xpath("//select/option[@value='Rádio']").click()
segmento = nav.find_element_by_xpath("//select/option[@value='Rádio']").text
sleep(1)

# Recupera opções do filtro de região
regioes = nav.find_elements_by_class_name("block-field-content").__getitem__(1).text.split('\n')
regioes.remove("Região")
# print("regiões: \n", regioes)

# Recupera opções do filtro de período
periodos = nav.find_elements_by_class_name("block-field-content").__getitem__(2).text.split('\n')
periodos.remove("Período")
# print("periodo: \n", periodos)

# Cria arquivo em branco com os campos: SEGMENTO, REGIAO, PERIODO, POSICAO_RANKING, MUSICA, COMPOSITOR"
arquivo = open("ranking_ecad.txt", "w")

# Varre o seletor de regiões
for regiao in regioes:
    # print(regiao)
    nav.find_element_by_xpath("//select/option[text()='"+regiao+"']").click()
    sleep(1)
    # Varre o seletor de período
    for periodo in periodos:
        # print(periodo)
        nav.find_element_by_xpath("//select/option[text()='" + periodo + "']").click()
        sleep(1)

        # Recupera conteúdo do ranking
        conteudo_ranking = nav.find_element_by_xpath("//*[(@id = 'lista-ranking')]").text
        ranking = conteudo_ranking.split('\n')

        # Armazena variaveis do filtro e do ranking referente aos filtros selecionados
        rank1 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[0:3]])
        rank2 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[3:6]])
        rank3 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[6:9]])
        rank4 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[9:12]])
        rank5 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[12:15]])
        rank6 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[15:18]])
        rank7 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[18:21]])
        rank8 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[21:24]])
        rank9 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[24:27]])
        rank10 = segmento + ',' + regiao + ',' + periodo + ',' + ','.join([str(v) for v in ranking[27:31]])

        # Armazena o conteúdo no arquivo
        with open("ranking_ecad.txt", "a") as arquivo:
            arquivo.write(rank1 + "\n")
            arquivo.write(rank2 + "\n")
            arquivo.write(rank3 + "\n")
            arquivo.write(rank4 + "\n")
            arquivo.write(rank5 + "\n")
            arquivo.write(rank6 + "\n")
            arquivo.write(rank7 + "\n")
            arquivo.write(rank8 + "\n")
            arquivo.write(rank9 + "\n")
            arquivo.write(rank10 + "\n")
