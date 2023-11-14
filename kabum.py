from bs4 import BeautifulSoup
import urllib.request
import requests
import json

url = input("Digite o Url da Kabum: ")

resultado = requests.get(url)
doc = BeautifulSoup(resultado.text, "html.parser")
urllib.request.urlretrieve(url, 'pagina.html')

nome = doc.find(class_="dVrDvy")
preco = doc.find(class_="finalPrice")
strNome = nome.string
strPreco = preco.string

produto_dado = {
            'nome': strNome,
            'preco': strPreco
}

'''export = json.dumps({"Nome": strNome, "Preco": strPreco}, ensure_ascii=False, indent=4)'''

with open('produtos.json', 'w') as _f:
    json.dump(produto_dado, _f, indent=4)
    '''dump = file'''
    '''dumps = string'''
    '''Load = file'''
    '''Loads = string'''


print(produto_dado)
