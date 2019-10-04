from django.urls import path
from . import views
urlpatterns = [
	path('',views.index, name='index'),path('add/<int:a>/<int:b>/',views.add, name='add'), path('login/<str:username>/',
	views.login, name='login')
]