from django.urls import path
from . import views
urlpatterns = [
    path('',views.loginPage,name="landing"),
    path('logout/',views.logoutUser,name="logout"),
    path('home/<str:user>',views.home,name="home"),
    path('create/<str:user>/<str:t>',views.create,name="create"),
    path('main/<str:user>/<str:pk>/<str:t>',views.upload,name="main"),
    path('shuffle/<str:user>/<str:pk>/<str:t>',views.shuffle,name="shuffle"),
    path('ss/',views.capture_region,name="ss")
]