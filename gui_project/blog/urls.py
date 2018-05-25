from django.urls import path

from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.index , name='index'),
    path('<int:dailylog_id>/', views.detail, name='detail'),
    path('category/<int:category_num>/', views.category, name='category'),
]




