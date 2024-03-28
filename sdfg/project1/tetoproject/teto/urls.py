from django.urls import path
from accounts import views

from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('teto/', views.ListPostView.as_view(), name="postlist"),
    path('teto/create', views.CreatePostView.as_view(), name="postcreate"),
    path('teto/<int:pk>/delete', views.DeletePostView.as_view(), name="postdelete"),
    path('teto/<int:pk>/detail', views.DetailPostView.as_view(), name="postdetail"),
    path('teto/<int:pk>/comment', views.CreateCommentView.as_view(), name="postcomment"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]