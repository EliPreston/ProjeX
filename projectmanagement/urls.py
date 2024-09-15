from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profilelist/', views.profilelist, name='profilelist'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('myprojects/', views.myprojects, name='myprojects'),
    path('explore/', views.explore, name='explore'),
    path('project/<int:projkey>', views.project, name='project'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('signup/', views.register, name='signup')
]
