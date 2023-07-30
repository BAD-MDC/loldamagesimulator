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
    atkspd = stats[5]
    ap = 0
    physical_dmg = 0
    magical_dmg = 0
    true_dmg = 0
    q_dmg = getChampionSkill(champion, "Q")
    w_dmg = getChampionSkill(champion, "W")
    e_dmg = getChampionSkill(champion, "E")
    r_dmg = getChampionSkill(champion, "R")
    getRealSkillDamage(getChampionSkill(champion,"E"),5, [ad,ad,ap,atkspd])



damageSimulator("Akali","qwer",13,"none","5512")

