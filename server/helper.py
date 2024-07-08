import requests


def getManagerData(id):
    response = requests.get("https://fantasy.premierleague.com/api/entry/" + str(id) + "/")
    if response.status_code == 200:
        return response.json()
    return None

def getHistory(id):
    response = requests.get("https://fantasy.premierleague.com/api/entry/" + str(id) + "/history/")
    if response.status_code == 200:
        return response.json()
    return None

def getTeamData(id, event):
    response = requests.get("https://fantasy.premierleague.com/api/entry/" + str(id) + "/event/" + str(event) + "/picks/")
    if response.status_code == 200:
        return response.json()
    return None

def getGeneralInfo():
    response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    if response.status_code == 200:
        return response.json()
    return None

def getPlayersGameweekPoints(event):
    response = requests.get("https://fantasy.premierleague.com/api/event/" + str(event) + "/live/")
    if response.status_code == 200:
        return response.json()
    return None