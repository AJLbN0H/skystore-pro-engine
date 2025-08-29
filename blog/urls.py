from django.urls import path
from blog.views import (
    BlogEntryCreateView,
    BlogEntryUpdateView,
    BlogEntryListView,
    BlogEntryDeleteView,
    BlogEntryDetailView,
)

app_name = "blog"

urlpatterns = [
    path("blogs/", BlogEntryListView.as_view(), name="blogs"),
    path("blogs/create/", BlogEntryCreateView.as_view(), name="blog_create"),
    path("blogs/update/<int:pk>/", BlogEntryUpdateView.as_view(), name="blog_update"),
    path("blogs/delete/<int:pk>/", BlogEntryDeleteView.as_view(), name="blog_delete"),
    path("blogs/detail/<int:pk>/", BlogEntryDetailView.as_view(), name="blog_detail"),
]
