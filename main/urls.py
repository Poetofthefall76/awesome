from django.urls import path
from . import views
from main.views import index

app_name = "main"
urlpatterns = [
    path("", views.MainPageView.as_view(), name="form_view"),
    path("new_page", index, name="new_page"),
    # path("new_page", index, name="new_page"),
    # path("new_page", index, name="new_page"),
    # path("new_page", index, name="new_page"),
    # path("new_page", index, name="new_page"),
]
