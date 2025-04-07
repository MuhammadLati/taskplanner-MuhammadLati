from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_time', 'end_time', 'purpose']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'purpose': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 4}
            )
        }
        labels = {
            'start_time': 'Alkamisaika',
            'end_time': 'Päättymisaika',
            'purpose': 'Käyttötarkoitus'
        } 