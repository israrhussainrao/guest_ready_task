from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Booking, Flat
from .forms import BookingForm, FlatForm
from rest_framework.response import Response


class BookingForReact(viewsets.ViewSet):
    def get(self, request):
        # we can use the out ref and sub query as well but the complex query always take time for long for big data.



        # Booking_objects = Booking.objects.filter(
        #     flat=OuterRef('flat'),
        #     checkout__lt=OuterRef('checkin')
        # )
        #
        # bookings_subquery_objects = Booking.objects.annotate(
        #     previous_booking_id=Subquery(Booking_objects.values('id').first()
        # ).order_by('flat')



        # Recommended approach
        # creating  DB store procedure usign SQL Alchemy

        # current approach is easy and simple but for big data it can be slow, but by using select_related we saved the multiple query to database
        bookings_objects = Booking.objects.select_related('flat').order_by('flat_id')
        previous_booking = {}
        booking_data = []

        for booking in bookings_objects:
            prev_booking_id = previous_booking.get(booking.flat_id, None)
            booking_data.append({
                'flat_name': booking.flat.name,
                'booking_id': booking.pk,
                'checkin': booking.checkin,
                'checkout': booking.checkout,
                'previous_booking_id': prev_booking_id,
            })
            previous_booking[booking.flat_id] = booking.pk
        return Response(booking_data)


def bookings(request):
    bookings_objects = Booking.objects.select_related('flat').order_by('flat_id', 'checkin')
    booking_list = []

    previous_booking = {}
    for booking in bookings_objects:
        prev_booking_id = previous_booking.get(booking.flat_id, None)
        booking_list.append({
            'flat_name': booking.flat.name,
            'booking_id': booking.pk,
            'checkin': booking.checkin,
            'checkout': booking.checkout,
            'previous_booking_id': prev_booking_id,
        })
        previous_booking[booking.flat_id] = booking.pk

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/bookings')
    else:
        form = BookingForm()
    return render(request, 'bookings/booking.html', {'bookings': booking_list, 'form': form})


def flat_booking_registry(request):
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/flat_register')
    else:
        form = FlatForm()

    flats = Flat.objects.all()
    return render(request, 'bookings/flat_registry.html', {'flats': flats, 'form': form})

