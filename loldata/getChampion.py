import requests
import json

def latest_version():
    version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    version_data = requests.get(version_url).json()
    latest_version = str(version_data[0])
    return latest_version


def champions():
    champions_data_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/en_US/champion.json"
    champions_data = requests.get(champions_data_url).json()
    return champions_data


def champion(champion_name):
    champion_data_url = "http://ddragon.leagueoflegends.com/cdn/" + latest_version() + "/data/en_US/champion/" + champion_name + ".json"
    champion_data = requests.get(champion_data_url).json()
    return champion_data

#LOL 폴더에 전체 챔피언 정보 JSON 파일 생성
def writeChampionsJSON() :
    with open('./champions/champions.json', 'w') as convert_file:
        json.dump(champions(), convert_file, ensure_ascii = False)

#LOL 폴더에 특정 챔피언 정보 JSON 파일 생성
def writeChampionJSON(champion_name) :
    champion_json_file_name = './champions/' + champion_name + '.json'
    with open(champion_json_file_name, 'w') as convert_file:
        json.dump(champion(champion_name), convert_file, ensure_ascii = False)

def writeChampionTXT(champion_name) :
    champion_txt_file_name = open('./champion_info/' + champion_name + '.txt', 'w')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['hp']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['hpperlevel']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['mp']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['mpperlevel']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['armor']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['armorperlevel']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['spellblock']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['spellblockperlevel']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['attackdamage']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['attackdamageperlevel']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['attackspeed']) + '\n')
    champion_txt_file_name.write(str(champion(champion_name)['data'][champion_name]['stats']['attackspeedperlevel']) + '\n')



for champ in champions()['data'] :
    writeChampionTXT(champ)
#    print(champ)
#    writeChampionJSON(champ)

#print(champion('Aatrox'))