import requests

API_KEY=open('API_KEY').read() # Aqui tienes que poner tu KEY  generada por google en el archivo API_KEY.
SEARCH_ID=open('SEARCH_ID').read() # Aqui tienes que poner tu SEARCH_ID  generada por google en el archivo SEARCH_ID.

query="Aqui lo que quieres buscar" # Aqui tienes que poner lo que quieres buscar.

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ID}&q={query}"

response=requests.get(url)
print(response.json())

