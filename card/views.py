from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Card
from .models import TrainingCard
from .models import AnswerCard
from .models import ExampleCard

def start(request):
    return render(request, 'card/start.html')
def home(request):
    trainingcards = TrainingCard.objects
    return render(request, 'card/home.html', {'trainingcards':trainingcards})

def train(request, trainingcard_id):
    answercard1 = AnswerCard.objects.get(pk=1)
    answercard2 = AnswerCard.objects.get(pk=2)
    trainingcard = get_object_or_404(TrainingCard, pk=trainingcard_id)
    return render(request, 'card/training.html', {'trainingcard':trainingcard, 'answercard1':answercard1,'answercard2':answercard2})

def training(request, trainingcard_id):
    if request.method == 'POST':
        answercard1 = AnswerCard.objects.get(pk=1)
        answercard2 = AnswerCard.objects.get(pk=2)
        cardmark = get_object_or_404(TrainingCard, pk=trainingcard_id)
        if '1' in request.POST:
            if cardmark.answer == 1:
                cardmark.correct += 1
            else:
                cardmark.wrong += 1
                return render(request, 'card/wrong.html', {'trainincard':cardmark})
        elif '2' in request.POST:
            if cardmark.answer == 2:
                cardmark.correct += 1
            else:
                cardmark.wrong += 1
                return render(request, 'card/wrong.html', {'trainincard':cardmark})
        cardmark.save()
        try:
            nextcard = TrainingCard.objects.get(pk=trainingcard_id+1)
        except TrainingCard.DoesNotExist:
            return redirect('../home')
        return render(request, 'card/training.html', {'trainingcard':nextcard, 'answercard1':answercard1, 'answercard2':answercard2})

def test(request):
    examplecard = ExampleCard.objects.get(pk=1)
    return render(request, 'card/test.html', {'example': examplecard})

def details(request, card_id):
    detailcard = get_object_or_404(Card, pk=card_id)
    answercard1 = AnswerCard.objects.get(pk=1)
    answercard2 = AnswerCard.objects.get(pk=2)
    return render(request, 'card/details.html', {'card':detailcard, 'answercard1':answercard1, 'answercard2':answercard2})

def correct(request, card_id):
    if request.method == 'POST':
        answercard1 = AnswerCard.objects.get(pk=1)
        answercard2 = AnswerCard.objects.get(pk=2)
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
        else:
            cardmark.runout += 1
        cardmark.save()
        try:
            nextcard = Card.objects.get(pk=card_id+1)
        except Card.DoesNotExist:
            return redirect('../../thanks')
        return render(request, 'card/details.html', {'card':nextcard, 'answercard1':answercard1, 'answercard2':answercard2})

def thanks(request):
    return render(request, 'card/thanks.html')
