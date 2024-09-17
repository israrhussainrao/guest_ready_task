# from rest_framework import serializers
# from .models import Booking
#
#
# class BookingListSerializer(serializers.ModelSerializer):
#     flat_name = serializers.CharField(source='flat.name', read_only=True)
#     previous_booking_id = serializers.IntegerField(read_only=True)
#
#     class Meta:
#         model = Booking
#         fields = ['flat_name', 'id', 'checkin', 'checkout', 'previous_booking_id']