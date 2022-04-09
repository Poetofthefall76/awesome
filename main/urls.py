from django.urls import path
from . import views
from main.views import completed, renovation, projects, house_construction, extensions

app_name = "main"
urlpatterns = [
    path("", views.MainPageView.as_view(), name="form_view"),
    path("completed", completed, name="completed"),
    path("renovation", renovation, name="renovation"),
    path("projects", projects, name="projects"),
    path("house_construction", house_construction, name="house_construction"),
    path("extensions", extensions, name="extensions"),
]
