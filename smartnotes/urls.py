from django.urls import path
from . import views

app_name = "smartnotes"

urlpatterns = [
    path("", views.index, name="index"),
    path("notes/", views.notes, name="notes"),
    path("notes/create/", views.note_create, name="note_create"),
    path("notes/<int:note_id>/", views.note_detail, name="note_detail"),
    path("notes/<int:note_id>/edit/", views.note_edit, name="note_edit"),
    path("notes/<int:note_id>/delete/", views.note_delete, name="note_delete"),
]
