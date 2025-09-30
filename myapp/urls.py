from django.urls import path
import myapp.views as myapp_views

urlpatterns = [
    path("", myapp_views.post_list, name="post_list")
]