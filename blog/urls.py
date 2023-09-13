from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name


urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='create_post'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail_post'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update_post'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_post'),
]
