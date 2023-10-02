import requests

# Your placeholder credentials
email = "ucabhgf@ucl.ac.uk"
password = "Trident!2023"

url = "https://query.api.nansen.ai/auth"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    "email": email,
    "password": password
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
