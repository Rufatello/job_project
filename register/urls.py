from django.urls import path
from . import views
from register.apps import RegisterConfig


app_name = RegisterConfig.name

urlpatterns = [
    path('', views.PatientListView.as_view(), name='home'),
    path('reg/', views.RegisterUser.as_view(), name='reg'),
    path('logout/', views.LogoutUser, name='logout'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('create_patient/', views.PatientCreateView.as_view(), name='create_patient'),
    path('update_patient/<int:pk>', views.PatientUpdateView.as_view(), name='update_patient'),
    path('delete_patient/<int:pk>', views.PatientDeleteeView.as_view(), name='delete_patient'),
]