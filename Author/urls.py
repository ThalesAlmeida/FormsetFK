from django.urls import path
from . import views
from enterprise.views import ServiceCreateView, ServiceListView

app_name = 'author'

urlpatterns = [
    path('', views.ProfileList.as_view(), name='profile-list'),
    path('profile/add', views.ProfileFamilyMemberCreate.as_view(), name='profile-add'),
    path('profile/<pk>/update', views.ProfileFamilyMemberUpdate.as_view(), name='profile-update'),
    path('profile/<pk>/delete', views.ProfileDelete.as_view(), name='profile-delete'),


    path('enterprise/add', ServiceCreateView.as_view(), name='enterprise-add'),
    path('enterprise', ServiceListView.as_view(), name='enterprise-list'),
    
]