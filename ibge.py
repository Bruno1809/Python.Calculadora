import requests, json

resultado = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/Bruno")

json_dados = json.loads(resultado.text)

print(json_dados[0]["res"][0])