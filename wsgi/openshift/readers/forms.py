from django import forms
from models import Reader

class NewReaderForm(forms.ModelForm):

    class Meta:
        model = Reader
        fields = ('raw_file',)
        
