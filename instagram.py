import requests

resposta = input('Qual tag você deseja consultar? ')
url = 'https://www.instagram.com/explore/tags/{}/?__a=1'.format(resposta)
resposta = requests.get(url)
dados = resposta.json()

print('Nome da tag: '+ dados['graphql']['hashtag']['name'])
print('Id: '+ dados['graphql']['hashtag']['id'])
print('Essa tag foi utilizada ' + str(dados['graphql']['hashtag']['edge_hashtag_to_media']['count']),'vezes')