from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),            # Исправлено: убраны скобки
    path('data/', views.datatext, name='data_text'), # Добавлен завершающий слэш
    path('test/', views.testtext, name='test_text'), # Добавлен завершающий слэш
]