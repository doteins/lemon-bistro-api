from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer

def index(request):
  return render(request, 'index.html', {})

class MenuView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = menuSerializer

class MenuDetailView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = Booking.objects.all()
  serializer_class = bookingSerializer
