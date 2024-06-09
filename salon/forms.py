from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['Name', 'Email', 'Password', 'Product_Nmae', 'resrv_Date', 'pay_method']
        widgets = {
            'Password': forms.PasswordInput(),
            'resrv_Date': forms.DateInput(attrs={'type': 'date'}),
        }
