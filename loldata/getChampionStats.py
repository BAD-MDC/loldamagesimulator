def getChampionData(champion_name):
    txt_name = "./champion_info/" + champion_name + ".txt"
    txt_file = open(txt_name, 'r')
    stats = txt_file.readlines()
    stats = [stat.rstrip('\n') for stat in stats]
    txt_file.close()
    return stats

def getChampionStats(champion_name, level):
    champion_data = getChampionData(champion_name)
    hp = float(champion_data[0]) + float(champion_data[1]) * (level - 1)
    mp = float(champion_data[2]) + float(champion_data[3]) * (level - 1)
    armor = float(champion_data[4]) + float(champion_data[5]) * (level - 1)
    spellblock = float(champion_data[6]) + float(champion_data[7]) * (level - 1)
    atkdmg = float(champion_data[8]) + float(champion_data[9]) * (level - 1)
    atkspd = float(champion_data[10]) + float(champion_data[11]) * (level - 1)
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

def getRealSkillDamage(skill_info,skill_level,champion_power):
    """
    :param skill_info: 스킬 데미지의 정보.
    :param skill_level: 스킬 레벨 정보
    :param champion_power: [총 공격력, 추가 공격력(총공격력 - 기본 공격력) , 주문력, 체력 ]
    :return:
    """
    if skill_info[0] == 'P':
        skill_type = 1
    elif skill_info[0] == 'M':
        skill_type = 2
    elif skill_info[0] == 'T':
        skill_type = 3
    else:
        return -1

    dmg = 0
    skills = (skill_info[2:]).split(' (')
    skill_regular_dmg = skills[0].split(' / ')
    dmg += float(skill_regular_dmg[skill_level - 1])


    for bonus_skill_dmg in skills[1:]:
        bonus = bonus_skill_dmg.split(' ')
        if len(bonus) > 5:
            bonus_percentage = 0.01 * float(bonus[2 * skill_level - 1].strip('%'))
        else:
            bonus_percentage = 0.01 * float(bonus[1].strip('%'))
        bonus_type = bonus[-1].strip(')')
        if bonus_type == 'bonus AD':
            dmg += champion_power[1] * bonus_percentage
        elif bonus_type == 'AD':
            dmg += champion_power[0] * bonus_percentage
        elif bonus_type == 'AP':
            dmg += champion_power[2] * bonus_percentage
        elif bonus_type == 'HP':
            dmg += champion_power[3] * bonus_percentage


    return dmg



#print(getChampionSkill("Ahri","q"))