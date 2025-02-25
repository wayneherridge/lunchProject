from django import forms
from .models import LunchItem, Student


class LunchItemForm(forms.ModelForm):
    class Meta:
        model = LunchItem
        fields = '__all__'
        # labels = {
        #     'lunch_item_id': 'Lunch Item ID',
        #     'lunch_date': 'Lunch Date',
        #     'student_name': 'Student Name',
        #     'lunch_option': 'Lunch Option',
        #     'other_option': 'Other Option',
        # }
        # widgets = {
        #     'lunch_item_id': forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
        #     'lunch_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'class':'form-control'}),
        #     'student_name': forms.TextInput(attrs={'placeholder': 'Select from list', 'class':'form-control'}),
        #     'lunch_option': forms.TextInput(attrs={'placeholder': 'Select from list', 'class':'form-control'}),
        #     'other_option': forms.TextInput(attrs={'placeholder': 'Cold wrap', 'class':'form-control'}),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student_name'].queryset = Student.objects.all()
