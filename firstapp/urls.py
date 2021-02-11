from django.urls import path
from . import views

urlpatterns = [
    path('search', views.search, name="search"),
    path('chart', views.chart, name="chart"),
    path('', views.home, name="home"),
    path('about', views.about, name='about'),
    path('table', views.table, name='table'),
    path('login', views.login, name='login'),
    path('firstapp/<int:id>', views.post_detail, name='post-detail'),
]