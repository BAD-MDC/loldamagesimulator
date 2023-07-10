from getChampion import champions
import json

def getChampionJsonFile(champion_name):
    json_file = "./champions/" + champion_name + ".json"
    with open(json_file, "r", encoding='utf-8') as champion_json:
        champion_json_data = json.load(champion_json)
    return champion_json_data

def getChampionStats(champion_name):
    json_file = getChampionJsonFile(champion_name)
    return json_file['data'][champion_name]['stats']

def getChampionSkills(champion_name):
    json_file = getChampionJsonFile(champion_name)
    return json_file['data'][champion_name]['spells']

def getChampionQ(champion_name):
    json_file = getChampionJsonFile(champion_name)
    return json_file['data'][champion_name]['spells'][0]

def getChampionW(champion_name):
    json_file = getChampionJsonFile(champion_name)
    return json_file['data'][champion_name]['spells'][1]

def getChampionE(champion_name):
    json_file = getChampionJsonFile(champion_name)
    return json_file['data'][champion_name]['spells'][2]

def getChampionR(champion_name):
    json_file = getChampionJsonFile(champion_name)
    return json_file['data'][champion_name]['spells'][3]

#스킬 데미지는 effect
#스킬 쿨타임은 cooldown