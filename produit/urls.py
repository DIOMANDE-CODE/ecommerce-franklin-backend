from django.urls import path
from .views import FruitList,FruitDetail,CategorieList,CategorieFruitDetail,ImageList

urlpatterns=[
    # url pour des fruits
    path('fruit/',FruitList.as_view()),
    path('fruit/<int:pk>/',FruitDetail.as_view()),

    # url des categories
    path('categorie/',CategorieList.as_view()),
    path('categorie/<int:pk>/',CategorieFruitDetail.as_view()),

    # url image
    path('image/',ImageList.as_view()),

]
