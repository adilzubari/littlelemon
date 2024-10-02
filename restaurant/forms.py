from django.forms import ModelForm
from .models import Booking
from django import forms
from django.core.exceptions import ValidationError


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'})
        }

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_slot = cleaned_data.get('reservation_slot')

        # Check if a booking already exists for the same date and time
        if Booking.objects.filter(reservation_date=reservation_date, reservation_slot=reservation_slot).exists():
            raise ValidationError('This time slot is already booked for the selected date.')

        return cleaned_data

