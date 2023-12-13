from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('studenthome/',views.studenthome,name='studenthome'),
    path('staffhome/',views.staffhome,name='staffhome'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('editorhome/',views.editorhome,name='editorhome'),
    path('logout/',views.logout,name='logout'),
    path('',views.login,name='login')]

