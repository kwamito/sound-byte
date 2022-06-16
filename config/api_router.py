from django.urls.conf import include, path

app_name = "api"
urlpatterns = (path("users/", include("api_project.users.urls")),)
