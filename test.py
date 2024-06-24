import requests

r = requests.get('https://www.olx.com.br/autos-e-pecas/carros-vans-e-utilitarios')

with open('403.html', 'w') as f:
    f.write(r.text)