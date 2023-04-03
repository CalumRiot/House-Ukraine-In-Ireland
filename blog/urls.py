from . import views
from django.urls import path
from .views import PostList, PostAbout, PostDetail, PostLike, PostUser, EditPostView, EditPostDetailView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.PostAbout.as_view(), name='about'),
    path('userpost/', views.PostUser.as_view(), name='user_post'),
    path('edit-posts/', EditPostView.as_view(), name='edit_posts'),
    path('edit-post/<int:pk>/', EditPostDetailView.as_view(), name='edit_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
