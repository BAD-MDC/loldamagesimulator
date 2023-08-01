from getChampionStats import *

########################################
#          DAMAGESIMULATOR RULE        #
# 1. 패시브는 데미지 계산 따로 진행         #
# 2. 스킬 데미지는 고정값 우선 처리         #
# 3. 추가 계수는 AD,AP 섞인 경우 순차 처리  #
# 4. 계수도 레벨에 비례한 경우 추가 처리     #
########################################
def damageSimulator(champion, combo, level, item, skill_level):
    stats = getChampionStats(champion,level)
    hp = stats[0]
    mp = stats[1]
    armor = stats[2]
    spellblock = stats[3]
    ad = stats[4]
    bonusad = 0
    atkspd = stats[5]
    ap = 0
    total_dmg = [0.0 , 0.0 , 0.0]
    q_dmg = getRealSkillDamage(getChampionSkill(champion,"Q"),int(skill_level[0]), [ad,bonusad,ap,atkspd])
    w_dmg = getRealSkillDamage(getChampionSkill(champion,"W"),int(skill_level[1]), [ad,bonusad,ap,atkspd])
    e_dmg = getRealSkillDamage(getChampionSkill(champion,"E"),int(skill_level[2]), [ad,bonusad,ap,atkspd])
    r_dmg = getRealSkillDamage(getChampionSkill(champion,"R"),int(skill_level[3]), [ad,bonusad,ap,atkspd])

    for skill in combo :
        for i in range (0,3) :
            if skill == 'q' or skill == 'Q' :
                total_dmg[i] = total_dmg[i] + q_dmg[i]
            elif skill == 'w' or skill == 'W' :
                total_dmg[i] = total_dmg[i] + w_dmg[i]
            elif skill == 'e' or skill == 'E' :
                total_dmg[i] = total_dmg[i] + e_dmg[i]
            elif skill == 'r' or skill == 'R' :
                total_dmg[i] = total_dmg[i] + r_dmg[i]

    print(total_dmg)



damageSimulator("Akali","qwer",13,"none","5152")

