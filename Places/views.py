from rest_framework import viewsets
from .models import Place, Categorie
from .serializer import PlaceSerializer, CategorieSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound




# Create your views here.


class CategorieViewset(viewsets.ModelViewSet):
    

    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer



class PlaceViewset(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        qs = Place.objects.all()
        print("ALL =>", qs)
        print("FILTERED =>", qs.filter(categorie_id=self.kwargs.get("categorie_pk")))
        return qs.filter(categorie_id=self.kwargs.get("categorie_pk"))
    
    def perform_create(self, serializer):
        categorie_id = self.kwargs.get('categorie_pk')
        try:
            categorie = Categorie.objects.get(id=categorie_id)
        except Categorie.DoesNotExist:
            raise NotFound("Catégorie inexistante") 

        serializer.save(categorie=categorie)