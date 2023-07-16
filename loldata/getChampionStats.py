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
    if skill == 'p' or 'P':
        index = 12
    if skill == 'q' or 'Q':
        index = 13
    if skill == 'w' or 'W':
        index = 14
    if skill == 'e' or 'E':
        index = 15
    if skill == 'r' or 'R':
        index = 16
    skill_info = getChampionData(champion_name)[index]
    skill_type = skill_info.split(' ', maxsplit=1)[0]
    skill_dmg = skill_info.split(' ', maxsplit=1)[1]
    if skill_type == 0 or skill_type == 'H' or skill_type == 'S':
        return 0
    return skill_dmg