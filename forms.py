from django import forms
from .models import employee,product

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'

class productForm(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'