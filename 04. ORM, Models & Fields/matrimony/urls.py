from django.urls import path
from . import views

app_name = 'matrimony'

urlpatterns = [
    path('', views.ProfileListView, name='profile_list'),
    path('<int:profile_id>', views.ProfileDetailView, name='profile_detail')
]