from django.urls import path
from . import views

urlpatterns = [
    # Paths del blog
    path('', views.blog, name="blog"),
    # Path filtro category
    path('category/<int:category_id>/', views.category, name="category"),
]