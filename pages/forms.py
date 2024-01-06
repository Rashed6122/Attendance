# face_recognition_app/forms.py
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    
class ExportAttendanceForm(forms.Form):
    month = forms.IntegerField(min_value=1, max_value=12)
    year = forms.IntegerField(min_value=2000, max_value=2100)