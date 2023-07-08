from rest_framework import serializers
from .models import Champion_stats

class Champion_stats_Serializer(serializers.ModelSerializer):
    class Meta:
        fields=('name','id','hp','hp_perlevel','mp','mp_perlevel','armor','armor_perlevel','spellblock','spellblock_perlevel','hpregen','hpregen_perlevel','mpregen','mpregen_perlevel','crit','crit_perlevel','attackdamage','attackdamage_perlevel','attackspeed','attackspeed_perlevel')
        model=Champion_stats