import requests
import subprocess

res = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY')


f = open('api.json', 'w')
f.write(res.text)

subprocess.run(['cat', 'api.json'])

