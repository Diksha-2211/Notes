from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        # for tag and color
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'tag': forms.TextInput(attrs={'placeholder': 'e.g. Personal, Study, Idea 💡'}),
        }
