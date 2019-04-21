from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Card

def home(request):
    return render(request, 'card/home.html')

def details(request, card_id):
    detailcard = get_object_or_404(Card, pk=card_id)
    return render(request, 'card/details.html', {'card':detailcard})
