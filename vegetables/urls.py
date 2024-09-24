# vegetables/urls.py
from django.urls import path
from .views import category_list, vegetable_list, vegetable_detail
from vegetables import views

urlpatterns = [
    # path('', category_list, name='category_list'),
    path('categories/', views.category_list, name='category_list'),
    # path('vegetables/', views.home, name='home'),
    path('category/category/<int:category_id>/', views.vegetable_list, name='vegetable_list'),
    path('vegetable/vegetable/<int:vegetable_id>/', views.vegetable_detail, name='vegetable_detail'),
    #  path('categories/', list_categories, name='list_categories'),
    # path('vegetables/<str:category_id>/', list_vegetables, name='list_vegetables'),
    
]


