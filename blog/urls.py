from django.urls import path
from blog import views


app_name = 'blog'

urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("<str:category>/", views.category, name="category"),
    ]
