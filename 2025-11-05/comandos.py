import requests

# Definindo a URL para fazer a requisição
strURL = 'http://www.globo.com'

# Definindo os cabeçalhos HTTP
dicHeaders = { 'User-Agent': 'MeuAppPython/1.0' }

try:
   # Fazendo a requisição GET
   response = requests.get(strURL, headers=dicHeaders)
except requests.exceptions.ConnectTimeout:
   print(f'\nERRO: A conexão demorou demais (Timeout). O servidor pode estar offline ou lento...\n')
except requests.exceptions.RequestException as e:
   print(f'\nERRO: Ocorreu um erro ao fazer a requisição: {e}\n')
except Exception as e:
   print(f'\nERRO: {e}\n')
else:
