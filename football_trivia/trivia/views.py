from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Score
from django.contrib.auth.models import User

# Create your views here.

"""
Renders a home page.
"""
def home(request):
    return render(request, 'home.html')


"""
Displays quiz.
Processes answers.
"""
@login_required
def quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                correct = Choice.objects.get(question=question, correct=True)
                if str(correct.id) == selected:
                    score += 1
        Score.objects.create(user=request.user, score=score)
        return render(request, 'result.html', 
                      {'score': score, 'total': len(questions)})
    return render(request, 'quiz.html', {'questions': questions})


"""
Displays logged in users score.
"""
@login_required
def profile(request):
    scores = Score.objects.filter(user=request.user).order_by('-taken_on')
    return render(request, 'profile.html', {'scores': scores})