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
    q_details = json_file['data'][champion_name]['spells'][0]
    q_effect = q_details['effect']
    q_damage = [0, 0, 0, 0, 0]
    for effect in q_effect :
        if effect == None:
            continue
        if effect[0] < effect[1] and effect[0] >= 10 :
            q_damage = effect
    return q_damage

def getChampionW(champion_name):
    json_file = getChampionJsonFile(champion_name)
    w_details = json_file['data'][champion_name]['spells'][1]
    w_effect = w_details['effect']
    w_damage = [0, 0, 0, 0, 0]
    for effect in w_effect:
        if effect == None:
            continue
        if effect[0] < effect[1] and effect[0] >= 10:
            w_damage = effect
    return w_damage
def getChampionE(champion_name):
    json_file = getChampionJsonFile(champion_name)
    e_details = json_file['data'][champion_name]['spells'][2]
    e_effect = e_details['effect']
    e_damage = [0, 0, 0, 0, 0]
    for effect in e_effect:
        if effect == None:
            continue
        if effect[0] < effect[1] and effect[0] >= 10:
            e_damage = effect
    return e_damage

def getChampionR(champion_name):
    json_file = getChampionJsonFile(champion_name)
    r_details = json_file['data'][champion_name]['spells'][3]
    r_effect = r_details['effect']
    r_damage = [0, 0, 0, 0, 0]
    for effect in r_effect:
        if effect == None:
            continue
        if effect[0] == 0:
            continue
        if effect[0] < effect[1] and effect[0] >= 10:
            r_damage = effect
    return r_damage

def print_champion_damage():
    for champ in champions()['data']:
        print(champ, end="")
        print("   Q:", end="")
        print(getChampionQ(champ), end="")
        print(" W:", end="")
        print(getChampionW(champ), end="")
        print(" E:", end="")
        print(getChampionE(champ), end="")
        print(" R:", end="")
        print(getChampionR(champ))

#스킬 데미지는 effect
#스킬 쿨타임은 cooldown

#print_champion_damage()