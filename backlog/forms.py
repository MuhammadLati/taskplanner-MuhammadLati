from django import forms
from .models import Task  

class TaskEditModelForm(forms.ModelForm):  
    class Meta:  
        model = Task  
        exclude = ['user']  # Don't allow direct user editing through the form
        labels = {
            'title': 'Otsikko',
            'description': 'Kuvaus',
            'completed': 'Valmis',
            'additional_info': 'Lisätiedot',
            'priority': 'Prioriteetti',
            'task_class': 'Tehtäväluokka'
        }  