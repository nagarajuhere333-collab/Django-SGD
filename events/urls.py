from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # Venue URLs
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/<slug:slug>/', views.venue_detail, name='venue_detail'),
    
    # Jewellery URLs
    path('jewellery/', views.jewellery_list, name='jewellery_list'),
    path('jewellery/<slug:slug>/', views.jewellery_detail, name='jewellery_detail'),
    
    # Food URLs
    path('food/', views.food_list, name='food_list'),
    path('food/<slug:slug>/', views.food_detail, name='food_detail'),
    
    # Favorites
    path('favorites/', views.favorites, name='favorites'),
    path('favorites/toggle/', views.toggle_favorite, name='toggle_favorite'),
]
