from . import views
from django.urls import path
from .views import PostList, PostAbout, PostDetail, PostLike, UserPostView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about', views.PostAbout.as_view(), name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('userpost', views.UserPostView.as_view(), name='user_post'),
]
