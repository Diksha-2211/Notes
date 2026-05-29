# notes/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard.html', {'notes': notes})

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('dashboard')
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})

@login_required
def update_note(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = NoteForm(instance=note)
    return render(request, 'update_note.html', {'form': form, 'note': note})

@login_required
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('dashboard')
    return render(request, 'delete_note.html', {'note': note})

