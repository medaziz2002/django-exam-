from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/',views.info ,name='info'),
    path('stage/',views.stage ,name='stage'),
    path('formation/',views.formation, name='formation'),
    path('competance/',views.competance, name='competance'),
    path('type/',views.type,name='type'),
    path('type/update_typ/<int:id>',views.update_typ,name='update_typ'),
    path('type/update_typ/update_typ_action/<int:id>',views.update_typ_action,name='update_typ_action'),
    path('type/addtype/', views.add_type, name='add_type'),
    path('type/addtype/add_type_action/', views.add_type_action, name='add_type_action'),
    path('type/delete_type/<int:id>',views.delete_type,name="delete_type"),
    path('formation/addformation/', views.add_formation, name='add_formation'),
    path('formation/addformation/add_formation_action/', views.add_formation_action, name='add_formation_action'),
    path('formation/delete_formation/<int:id>',views.del_formation,name="delete_formation"),
    path('formation/update_formation/<int:id>',views.update_formation,name='update_formation'),
    path('formation/update_formation/update_formation_action/<int:id>',views.update_formation_action,name='update_formation_action'),
    path('connexion/', views.connect, name='connect'),
    path('connexion/login/', views.signIn, name='signIn'),
    path('connexion/login/login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect'),
]