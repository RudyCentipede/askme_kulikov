import copy
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

QUESTIONS = [
    {
        'title': 'title ' + str(i),
        'id': i,
        'text': 'This is text for question # ' + str(i)
    } for i in range(1, 30)
]


def index(request):
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(QUESTIONS, 5)
    page = paginator.page(page_num)
    return render(request, 'index.html', context={'questions': page.object_list, 'page_obj': page})


def hot(request):
    hot_questions = copy.deepcopy(QUESTIONS)
    hot_questions.reverse()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(hot_questions, 5)
    page = paginator.page(page_num)
    return render(request, 'hot.html', context={'questions': page.object_list, 'page_obj': page})


def question(request, question_id):
    one_question = next((q for q in QUESTIONS if q['id'] == question_id), None)
    if one_question is None:
        return render(request, '', status=404)
    return render(request, 'question.html', context={'question': one_question})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def settings(request):
    return render(request, 'settings.html')


def ask(request):
    return render(request, 'ask.html')

