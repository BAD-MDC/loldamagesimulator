from getChampionStats import *

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




damageSimulator("Aatrox","qwer",13,"none","5512")

