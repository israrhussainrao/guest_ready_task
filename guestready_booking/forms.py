from django import forms
from .models import Booking, Flat


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['flat', 'checkin', 'checkout']


class FlatForm(forms.ModelForm):
    class Meta:
        model = Flat
        fields = ['name']