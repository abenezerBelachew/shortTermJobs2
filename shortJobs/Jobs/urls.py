from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'), # The home page
    path('addJobPost/', views.AddEntryView.as_view(), 
        name = 'addJob'),
    path('tag/<slug:tag_slug>/',
        views.index, name='post_list_by_tag'),
    path('register/', views.register, name='register'),
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
