from django.urls import path
from . import views


urlpatterns = [
    #path('',views.index),
    path('category/<str:slug>/', views.category_page),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('feedback/',views.feedback_page),
    path('team/',views.team_page),
    path('create_team/',views.TeamCreate.as_view()),
    path('team/<int:pk>/',views.team_page),
    path('team_apply/', views.team_apply_page)
    #path('<int:pk>/', views.single_post_page),
]
