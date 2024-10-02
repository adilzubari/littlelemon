# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Menu
from .models import Booking
from django.http import JsonResponse
from django.core.serializers import serialize
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations')
    context = {'form':form}
    return render(request, 'book.html', context)

def reservations(request):
    bookings = Booking.objects.all()
    bookings_json = serialize('json', bookings)
    if not bookings:  # Check if there are no bookings
        no_bookings_message = "No bookings available."
    else:
        no_bookings_message = ""

    context = {
        'bookings_json': bookings_json,
        'no_bookings_message': no_bookings_message,
    }
    
    return render(request, 'reservations.html', context)

def date_specific_bookings(request):
    date_str = request.GET.get('date')
    if date_str:
        try:
            booking_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            bookings = Booking.objects.filter(reservation_date=booking_date).values()
            
            if not bookings:  # Check if bookings list is empty
                return JsonResponse({'message': 'No bookings available for this date.'}, status=200)
                
            return JsonResponse(list(bookings), safe=False)
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
    else:
        return JsonResponse({'error': 'Date parameter is required.'}, status=400)

def menu(request):
    menu_data = Menu.objects.all().order_by("name")
    main_data = {"menu" : menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    context = {"menu_item" : menu_item}
    return render(request, 'menu_item.html', context)