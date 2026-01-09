# urls.py
from rest_framework_nested import routers 
from .views import PlaceViewset, CategorieViewset

router = routers.SimpleRouter()
router.register('categories', CategorieViewset , basename='categories')

categories_router = routers.NestedSimpleRouter(
    router, 'categories', lookup='categorie'
)
categories_router.register(
    'places', PlaceViewset, basename='categorie-places'
)

urlpatterns = router.urls + categories_router.urls

