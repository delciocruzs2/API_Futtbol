import requests

url = "https://api.api-futebol.com.br/v1/campeonatos/"

headers = {
    "Authorization": "Bearer live_5212a6ff5a9a64ea6e882be1cec74f"
}

# Fazendo a requisição GET
response = requests.get(url, headers=headers)





if __name__ == '__main__':
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f" Erro na requisição: {response.status_code}")
        print(response.text)



