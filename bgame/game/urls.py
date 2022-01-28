from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    # /game/
    path('', views.index, name='index'),
    path('weapons/', views.weapons, name='weapons-index'),
    path('weapons/create/', views.weapons_create, name='weapons-create'),
    path('weapons/store/', views.weapons_store, name='weapons-store'),
    path('armors/', views.armors, name='armors-index'),
    path('armors/create/', views.armors_create, name='armors-create'),
    path('armors/store/', views.armors_store, name='armors-store'),
    path('characters/', views.characters, name='characters-index'),
    path('characters/create/', views.characters_create, name='characters-create'),
    path('characters/store/', views.characters_store, name='characters-store'),
]