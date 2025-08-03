# listings/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets, filters, status
from .models import Listing,Booking
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
class SampleAPIView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel App"})
