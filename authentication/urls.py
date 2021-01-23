from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('CustomUser', views.CustomUserView)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.all_users, name='users'),
    path('<int:id>/', views.user_form, name='user'),
    path('<int:id>/view', views.user_by_id, name='user_by_id'),
    path('<int:id>/delete/', views.user_delete, name='user_delete'),
]
