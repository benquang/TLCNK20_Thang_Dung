from rest_framework import serializers
from .models import *

class Matchs_Dataset_Model(serializers.ModelSerializer):
    class Meta:
        model = Fbref_Matchplayerstats_Modified
        fields = '__all__'

class Fbref_Matchgoals_Modified(serializers.ModelSerializer):
    class Meta:
        model = Fbref_Matchgoals_Modified
        fields = '__all__'

class Fbref_Matchinfos_Modified(serializers.ModelSerializer):
    class Meta:
        model = Fbref_Matchinfos_Modified
        fields = '__all__'

class Fbref_Matchplayerstats_Modified(serializers.ModelSerializer):
    class Meta:
        model = Fbref_Matchplayerstats_Modified
        fields = '__all__'
class Fbref_Matchsquad_Modified(serializers.ModelSerializer):
    class Meta:
        model = Fbref_Matchsquad_Modified
        fields = '__all__'

