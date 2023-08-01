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
        if si[0] == 'P' or si[0] == 'M' or si[0] == 'T':
            damages.append(si)
        else:
            continue
    return damages

def getRealSkillDamage(damages,skill_level,champion_power):
    """
    :param damages: 스킬 데미지의 정보.
    :param skill_level: 스킬 레벨 정보
    :param champion_power: [총 공격력, 추가 공격력(총공격력 - 기본 공격력) , 주문력, 체력 ]
    :return: [ 물리 데미지 총량, 마법 데미지 총량, 고정 데미지 총량 ]
    """
    result = [0.0, 0.0, 0.0]
    if damages == [] :
        return result

    if skill_level == 0 :
        return result

    for damage in damages:
        damage_split = damage.split('# ')

        damage_values = damage_split[1].split('(+ ')
        pure_dmg = damage_values[0].split(' / ')
        final_dmg = float(pure_dmg[skill_level-1])
        for dmg in damage_values:
            dmg_values = dmg.split(' / ')
            if dmg_values == pure_dmg:
                continue
            #추가 계수가 레벨에 비례하지 않은 경우
            if len(dmg_values) == 1:
                bonus_percentage = dmg_values[0].split(' ')[0]
                bonus_damage_type = dmg_values[0].split(' ')[1].split(')')[0]
            #추가 계수가 레벨에 따라 달라지는 경우
            else :
                if skill_level == len(dmg_values):
                    bonus_percentage = dmg_values[skill_level - 1].split(' ')[0]
                else :
                    bonus_percentage = dmg_values[skill_level - 1]
                bonus_damage_type = dmg_values[-1].split(' ')[1].split(')')[0]


            bonus_percentage = float(bonus_percentage.strip('%')) / 100
            if bonus_damage_type == 'AD':
                final_dmg = final_dmg + champion_power[0] * bonus_percentage
            elif bonus_damage_type == 'bonusAD':
                final_dmg = final_dmg + champion_power[1] * bonus_percentage
            elif bonus_damage_type == 'AP':
                final_dmg = final_dmg + champion_power[2] * bonus_percentage
            elif bonus_damage_type == 'AS':
                final_dmg = final_dmg + champion_power[3] * bonus_percentage

        if damage_split[0] == 'P':
            result[0] = result[0] + final_dmg
        elif damage_split[0] == 'M':
            result[1] = result[1] + final_dmg
        elif damage_split[0] == 'T':
            result[2] = result[2] + final_dmg

    return result


#print(getChampionSkill("Ahri","q"))