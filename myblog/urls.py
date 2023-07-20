from django.contrib import admin
from django.urls import path, include
from blog.views import MainView, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostSearchView, RegisterView, LoginView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/write/', PostCreateView.as_view(), name='post_create'),
    path('blog/edit/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('blog/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('blog/search/<str:tag>/', PostSearchView.as_view(), name='post_search'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
]
