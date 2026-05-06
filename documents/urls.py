from django.urls import path
from .views import UploadDocumentView, SearchView

urlpatterns = [
    path('upload/', UploadDocumentView.as_view()),
    path('search/', SearchView.as_view()),
]