def getChampionData(champion_name):
    txt_name = "./champion_info/" + champion_name + ".txt"
    txt_file = open(txt_name, 'r')
    stats = txt_file.readlines()
    stats = [stat.rstrip('\n') for stat in stats]
    txt_file.close()
    return stats

def getChampionStats(champion_name, level):
    champion_data = getChampionData(champion_name)
    hp = champion_data[0] + champion_data[1] * (level - 1)
    mp = champion_data[2] + champion_data[3] * (level - 1)
    armor = champion_data[4] + champion_data[5] * (level - 1)
    spellblock = champion_data[6] + champion_data[7] * (level - 1)
    atkdmg = champion_data[8] + champion_data[9] * (level - 1)
    atkspd = champion_data[10] + champion_data[11] * (level - 1)
    return [hp, mp, armor, spellblock, atkdmg, atkspd]

def getChampionSkill(champion_name, skill):
    if skill == 'p' or skill == 'P':
        index = 12
    elif skill == 'q' or skill == 'Q':
        index = 13
    elif skill == 'w' or skill == 'W':
        index = 14
    elif skill == 'e' or skill == 'E':
        index = 15
    elif skill == 'r' or skill == 'R':
        index = 16
    damages = []
    skill_info = getChampionData(champion_name)[index]
    skill_index = skill_info.split(' + ')
    for si in skill_index:
        if si[0] == 0 or si[0] == 'B' or si[0] == 'S':
            continue
        else:
            damages.append(si)
    return damages

#print(getChampionSkill("Ahri","q"))