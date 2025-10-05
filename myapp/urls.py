from django.urls import path
import myapp.views as myapp_views

urlpatterns = [
    path("authors/", myapp_views.author_list, name="author_list"),
    path("authors/<int:author_id>/", myapp_views.get_author_by_id, name="author_detail"),
    path("posts/", myapp_views.post_list, name="posts_list"),
    path("posts/<int:post_id>/", myapp_views.get_post_by_id, name="post_detail"),
    path("test/", myapp_views.test, name="test"),
]