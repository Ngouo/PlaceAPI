from .models import Place, Categorie
from rest_framework import serializers



class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "nom_place", "ville", "indication", "pseudo"]

    

class CategorieSerializer(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    class Meta:
        model = Categorie
        fields = '__all__'