from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BlogsByAuthorListView.as_view(), name='blog-by-author'),
    path('<int:pk>/comment',views.add_comment_to_blog, name='add-comment'),
    path('delete/<int:comment_id>',views.delete_comment, name='delete-comment'),
]


# primary key 1 of blog is not available because I deleted the first blog before. need to resolve this problem later