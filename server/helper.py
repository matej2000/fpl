import requests


def getManagerData(id):
    response = requests.get("https://fantasy.premierleague.com/api/entry/" + str(id) + "/")
    if response.status_code == 200:
        return response.json()
    return None