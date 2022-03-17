from django.urls import path
from . import views

urlpatterns = [
    path('',views.LandingView.as_view(),name='test'),
    path('create/post/',views.CreatePostView.as_view(),name='create-post'),
    path('posts_list/',views.ListPostView.as_view(),name='post-list'),
    path('post_details/<int:pk>', views.DetailPostView.as_view(),name='post-details'),
    path('post/<int:pk>/delete/',views.DeletePostView.as_view(),name='post-delete'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(),name='post-update'),
    path('post/<int:pk>/like', views.add_like,name='post-like'),
    path('comment/<int:pk>/create/',views.CreateCommentView.as_view(),name='create-comment'),
    # Categories paths
    path('search/category/',views.search_category_view,name='search-category'),

]
