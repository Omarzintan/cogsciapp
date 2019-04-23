from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Card
from .models import TrainingCard

def start(request):
    return render(request, 'card/start.html')
def home(request):
    trainingcards = TrainingCard.objects
    return render(request, 'card/home.html', {'trainingcards':trainingcards})

def train(request, trainingcard_id):
    trainingcard = get_object_or_404(TrainingCard, pk=trainingcard_id)
    return render(request, 'card/training.html', {'trainingcard':trainingcard})

def training(request, trainingcard_id):
    if request.method == 'POST':
        cardmark = get_object_or_404(TrainingCard, pk=trainingcard_id)
        if '1' in request.POST:
            if cardmark.answer == 1:
                cardmark.correct += 1
            else:
                cardmark.wrong += 1
        elif '2' in request.POST:
            if cardmark.answer == 2:
                cardmark.correct += 1
            else:
                cardmark.wrong += 1
        cardmark.save()
        try:
            nextcard = TrainingCard.objects.get(pk=trainingcard_id+1)
        except TrainingCard.DoesNotExist:
            return redirect('../home')
        return render(request, 'card/training.html', {'trainingcard':nextcard})

def test(request):
    return render(request, 'card/test.html')

def details(request, card_id):
    detailcard = get_object_or_404(Card, pk=card_id)
    return render(request, 'card/details.html', {'card':detailcard})

def correct(request, card_id):
    if request.method == 'POST':
        cardmark = get_object_or_404(Card, pk=card_id)
        if '1' in request.POST:
            if cardmark.answer == 1:
                cardmark.correct += 1
            else:
                cardmark.wrong += 1
        elif '2' in request.POST:
            if cardmark.answer == 2:
                cardmark.correct += 1
            else:
                cardmark.wrong += 1
        cardmark.save()
        try:
            nextcard = Card.objects.get(pk=card_id+1)
        except Card.DoesNotExist:
            return redirect('../../thanks')
        return render(request, 'card/details.html', {'card':nextcard})

def thanks(request):
    return render(request, 'card/thanks.html')
