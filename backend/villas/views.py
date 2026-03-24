from django.shortcuts import render, get_object_or_404
from .models import Villa, Booking
from django.contrib.auth.decorators import login_required

def villa_list(request):
    villas = Villa.objects.filter(is_available=True)
    return render(request, 'villas/index.html', {'villas': villas})

def villa_detail(request, pk):
    villa = get_object_or_404(Villa, pk=pk)
    return render(request, 'villas/detail.html', {'villa': villa})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'villas/bookings.html', {'bookings': bookings})
