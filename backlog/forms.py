from django import forms
from .models import Task, TaskClass

class TaskEditModelForm(forms.ModelForm):
    title = forms.CharField(
        label='Otsikko',
        widget=forms.TextInput(attrs={'placeholder': 'Syötä tehtävän otsikko'})
    )
    description = forms.CharField(
        label='Kuvaus',
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'Syötä tehtävän kuvaus'
        })
    )
    task_class = forms.ModelChoiceField(
        label='Tehtävän tila',
        queryset=TaskClass.objects.all(),
        empty_label=None
    )
    priority = forms.ChoiceField(
        label='Prioriteetti',
        choices=[
            ('high', 'Korkea'),
            ('medium', 'Keskitaso'),
            ('low', 'Matala')
        ]
    )
    additional_info = forms.CharField(
        label='Lisätiedot',
        required=False,
        widget=forms.Textarea(attrs={
            'rows': 3,
            'placeholder': 'Syötä mahdolliset lisätiedot'
        })
    )
    completed = forms.BooleanField(
        label='Valmis',
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'task_class', 'priority', 'completed', 'additional_info']  