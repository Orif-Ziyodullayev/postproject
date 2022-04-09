from django.urls import path, include
from .views import (
    PostView,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete
)





urlpatterns = [

    path('',PostView.as_view(),name='home'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('post/new/',PostCreate.as_view(),name='post_new'),
    path('post/<int:pk>/update',PostUpdate.as_view(),name='post_update'),
    path('post/<int:pk>/delete',PostDelete.as_view(),name='post_delete')
]
