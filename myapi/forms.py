from django import forms
from .models import Hero

class DateInput(forms.DateInput):
    input_type = 'date'

class MovieForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = "__all__"
        widgets = {
            'starting_date': DateInput(),
            'ending_date': DateInput(),
            
        }
        
       
	




