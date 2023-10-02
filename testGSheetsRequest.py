import requests

def call_refresh_all():
    url = "http://165.232.104.175:5000/api/refresh_all"
    response = requests.post(url)

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print("Failed:", response.json())

if __name__ == "__main__":
    call_refresh_all()
