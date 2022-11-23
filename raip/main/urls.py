from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_patient/', views.all_patient, name='all'),
    path('profile/<slug:slug>/', views.profile, name='profile'),
    path('create_patient/', views.create_patient, name='create'),
    path(
        'update_patient/<int:patient_id>/',
        views.update_patient,
        name='update'
    ),
    path('predictImage/', views.predictImage, name='predictImage'),
    path('<slug:slug>/create_vkr/', views.create_vkr, name='create_vkr'),
    path(
        '<slug:slug>/update_vkr/<int:vkr_id>/',
        views.update_vkr,
        name='update_vkr'
    ),

    path('search/', views.SearchResultsView.as_view(), name='search_results')
]
