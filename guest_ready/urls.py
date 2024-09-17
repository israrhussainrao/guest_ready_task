"""
URL configuration for guest_ready project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from guestready_booking.views import bookings, flat_booking_registry, BookingForReact
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'bookings', BookingForReact, basename='booking')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', bookings, name='booking_list'),
    path('flat_register/', flat_booking_registry, name='add_flat'),
    path('api/bookings/', BookingForReact.as_view({'get': 'get'}), name='booking-list-api'),
    path('api/', include(router.urls)),
]