from django.urls import path
from . import views

app_name = 'author'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile-list'),
    path('profile/add', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    path('profile/<pk>/update', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    path('profile/<pk>/delete', views.ProfileDelete.as_view(), name='profile-delete'),
    
]