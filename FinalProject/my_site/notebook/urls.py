from django.urls import path, include
from .views import *


urlpatterns = [
    path('', select, name='select'),
    path('notebook/', NotesListView.as_view(), name='n_home'),
    path('notebook/about', about, name='n_about'),
    path('notebook/create', create, name='n_create'),
    path('notebook/note-<int:pk>', NotesDetailView.as_view(), name='n_note'),
    path('notebook/note-<int:pk>/update', NotesUpdateView.as_view(), name='n_update'),
    path('notebook/note-<int:pk>/delete', NotesDeleteView.as_view(), name='n_delete'),
]
