from bs4 import BeautifulSoup
import requests
import json

headers = {"Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.26.0",
  }

#url = input("Digite a Url: ")
url = 'https://www.submarino.com.br/headers'
resultado = requests.get(url, headers=headers)
with open("submarino.html", "w") as arquivo:
    arquivo.write(resultado.text)

doc = BeautifulSoup(resultado.text, "html.parser")



'''
nome = doc.find(class_="sc-kpDqfm gXZPqL")
preco = doc.find(class_="sc-kpDqfm eCPtRw sc-hoLEA kXWuGr")

strNome = nome.string
strPreco = preco.string

print(json.dumps({"Nome": strNome, "Preco": strPreco}, sort_keys=True, indent=4))
'''