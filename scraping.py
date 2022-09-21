import requests
from bs4 import BeautifulSoup
import pandas as pd


url_mercado_livre = "https://www.mercadolivre.com.br"
response = requests.get(url_mercado_livre)

status_code = response.status_code
print(f'STATUS CODE {status_code}\n')

mercado_livre_html = response.text
soup = BeautifulSoup(mercado_livre_html, "html.parser")


produtos = soup.find(class_="slick-track")
produtos = produtos.find_all("div", class_="slick-slide slick-active")


nomes = []
for produto in produtos:
  nome = produto.find(class_="ui-item__title").text
  nomes.append(nome)


precos = []
parcelas = []
total_parcelados = []

for produto in produtos:
  preco = produto.find(class_="price-tag ui-item__price")    
  preco = preco.find(class_="price-tag-fraction").text
  precos.append(preco)

  parcela = produto.find(class_="ui-item__installments").text
  parcelas.append(parcela)

  total_parcelado = parcela.split(" ")

  if "sem" in total_parcelado:
    multiplicacao = preco
  else:
    vezes = total_parcelado[0].split("x")[0]
    valor = total_parcelado[2]
    multiplicacao = int(vezes) * int(valor)

  total_parcelados.append(multiplicacao)


dicionario = {'PRODUTOS': nomes,'PRECOS': precos, 'PARCELAS': parcelas, 'TOTAL_PARCELADO': total_parcelados} 
df = pd.DataFrame(dicionario) 
print(df)