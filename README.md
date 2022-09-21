# 🛒 scraping-mercado-livre

Scraping com Python + Beautiful Soup + Requests + Pandas

Pegando os 5 produtos disponibilizados em "Oferta do dia" no Mercado Livre. 

Com Pandas, criamos um Dataframe ordenado por Produto, Preço, Parcela, e Total parcelado.

### ✴️ Exemplo de saída do Dataframe: 
```bash
                                            PRODUTOS  PRECOS               PARCELAS  TOTAL_PARCELADO
0   Samsung Galaxy A13 Dual SIM 128 GB azul 4 GB RAM   1.199   10x R$ 119 sem juros            1.199
1  Micro-ondas 32l Branco Com Menu Fácil Cms46ab ...     599    10x R$ 59 sem juros              599
2  Máquina De Acabamento Faz Pezinho Risco Desenh...      69               12x R$ 6               72
3  Smart Tv 50'' 4k Uhd Android Tv 50pug7406 Philips   2.499   10x R$ 249 sem juros            2.499
4     Kit Cuecas Box Boxer 10 Peças Original Atacado      86               12x R$ 8               96
```

### 📑 Tecnologias usadas:
<table>
  <tr>
    <td>Python</td>
    <td>Beautiful Soup</td>
    <td>Requests</td>
    <td>Pandas</td>
  </tr>
  <tr>
    <td>3.*</td>
    <td>4.11</td>
    <td>2.28</td>
    <td>1.5</td>
  </tr>
</table>

### 🔨 Como executar:

1) Clone o repositório e vá para a sua pasta:
```
$ git clone https://github.com/RakelMacedo/scraping-mercado-livre.git

$ cd scraping-mercado-livre/
```

2) No terminal, vamos criar e ativar nosso ambiente virtual:

```bash
$ python3 -m venv venv

$ source venv/bin/activate
```

3) Em seguida, vamos baixar as bibliotecas que iremos utilizar:

```bash
$ pip install -r requirements.txt
```

4) Agora rode o código: 
```bash
$ python scraping.py
```
##

❕ Caso o código não funcione, verifique as classes utilizadas para o scraping, sites tendem a mudar e com as mudanças precisamos dar manuntenção em nossos scrapings.

✅ Prontinho! Faça bom uso =D
