from django.db import models

# Create your models here.

class Champion_stats(models.Model):
    name=models.CharField(max_length=200,primary_key=True)
    hp=models.IntegerField()
    hp_perlevel=models.IntegerField()
    mp=models.IntegerField()
    mp_perlevel=models.IntegerField()
    armor=models.IntegerField()
    armor_perlevel=models.IntegerField()
    spellblock=models.IntegerField()
    spellblock_perlevel=models.IntegerField()
    hpregen=models.IntegerField()
    hpregen_perlevel=models.IntegerField()
    mpregen=models.IntegerField()
    mpregen_perlevel=models.IntegerField()
    crit=models.IntegerField()
    crit_perlevel=models.IntegerField()
    attackdamage=models.IntegerField()
    attackdamage_perlevel=models.IntegerField()
    attackspeed=models.IntegerField()
    attackspeed_perlevel=models.IntegerField()

class test(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=128)
    combo=models.CharField(max_length=128)
    level=models.IntegerField(default=1)
    item=models.CharField(max_length=128)