from django.urls import path
from .views import (
    PostListView,
    MyListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views

urlpatterns = [
    path('user-home/', views.user_home, name='user-home'),
    path('pool/', views.post_list, name='blog-home'),
    # path('zone/', MyListView.as_view(), name='my-space'),
    path('zone/', views.my_list, name='my-space'),
    path('my-profile/', views.my_profile, name='my-profile'),
    path('tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    # path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/profile/<int:pk>', views.user_profile, name='user-profile'),
    path('user/follower/', views.user_follower, name='user-follower'),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

