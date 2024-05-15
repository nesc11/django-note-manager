from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


# Create your views here.
def index(request):
    print(request.path)
    return render(request, "smartnotes/index.html")


@login_required
def notes(request):
    notes = Note.objects.filter(owner=request.user)
    return render(request, "smartnotes/notes.html", {"notes": notes})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    return render(request, "smartnotes/note_detail.html", {"note": note})


@login_required
def note_create(request):
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect("smartnotes:notes")
    return render(request, "smartnotes/note_create.html", {"form": form})


@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("smartnotes:notes")
    return render(request, "smartnotes/note_edit.html", {"form": form, "note": note})


@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    note.delete()
    return redirect("smartnotes:notes")
