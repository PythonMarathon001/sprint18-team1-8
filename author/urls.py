from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Author', views.AuthorView)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.all_authors, name='authors'),
    path('<int:id>/', views.author_form, name='author'),
    path('<int:id>/view', views.author_by_id, name='author_by_id'),
    path('<int:id>/delete/', views.author_delete, name='author_delete'),
]
