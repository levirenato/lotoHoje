import requests
from bs4 import BeautifulSoup

# urls
url = 'https://loteriadacaixa.net.br/'

# request
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
html = requests.get(url, headers=header)

# Start soup
s = BeautifulSoup(html.content, 'html.parser')

# Select div with content
div = s.find(class_='status-publish')

# Create a list of games, *and remove loteria federal game*
game = [game.text for game in div.find_all('h3')]
del game[7]

# list of winning lotto number
numbers = [game.text for game in div.find_all('span')]
mais_milionario = div.find('div', attrs={'style': "font-size: 1.3em;margin-bottom:20px;"}).text
mes_da_sorte = [i.text for i in div.find_all('p')][-2:]
# winning lotto number per game
results = [[numbers[:6], mais_milionario], numbers[6:12],
           numbers[12:27], numbers[27:32],
           numbers[32:52], [numbers[52:59], mes_da_sorte[0]],
           numbers[59:71], [numbers[71:78], mes_da_sorte[1]],
           numbers[78:]]

# created a dict with
data = dict(zip(game, results))
