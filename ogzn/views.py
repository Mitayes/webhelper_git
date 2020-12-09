from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Questions, GraphSelector
from django.http import JsonResponse


def index(request):
    request.session['path'] = ''
    return render(request, 'index.html', {'test': 'test text'})


def congratulations(request):
    return render(request, 'congratulations.html')


def start(request):
    dictt = {}
    # Получаем информацию о том, на каком вопросе (вершине) находится пользователь через GET запрос с templates
    nextq = request.GET.get('nextq', 'start')
    # Пользовательская переменная path нужна для сохранения маршрута, который прошёл посетитель
    if request.session['path'] == '':
        request.session['path'] += nextq
    else:
        request.session['path'] += ',' + nextq
    # Получаем информацию о том, куда можно перейти по графу из текущей вершины (следующие вопросы)
    near_nodes = list(GraphSelector.G.adj[nextq])
    for value in near_nodes:
        dictt['yes' in GraphSelector.G[nextq][value]] = value
    # Определяем сколько вариантов перемещения дальше имеется
    # Необходимо для вариативной отрисовки кнопок в templates
    next_count = len(list(GraphSelector.G.adj[nextq]))
    next_yes = ''
    next_no = ''
    next_next = ''
    nextq_id_yes = ''
    nextq_id_no = ''
    nextq_id_next = ''
    if next_count == 0:
        pass
    elif next_count == 1:
        # По умолчанию если предполагается 1 вариант ответа на ребро ставится метка yes
        next_next = Questions.objects.get(quest_id=dictt.get(True))
        nextq_id_next = dictt.get(True)
    elif next_count == 2:
        # Получаем из графа текст для ответа ДА
        next_yes = Questions.objects.get(quest_id=dictt.get(True))
        # Получаем из графа текст для ответа НЕТ
        next_no = Questions.objects.get(quest_id=dictt.get(False))
        # Получаем идентификаторы для ДА и НЕТ для кнопок в форме
        nextq_id_yes = dictt.get(True)
        nextq_id_no = dictt.get(False)
    context = {
        'question': Questions.objects.get(quest_id=nextq),
        'comment': ', '.join(Questions.objects.filter(quest_id=nextq).values_list('quest_comment', flat=True)),
        'nextq_yes': next_yes,
        'nextq_no': next_no,
        'next_next': next_next,
        'next_count': next_count,
        'nextq_id_yes': nextq_id_yes,
        'nextq_id_no': nextq_id_no,
        'nextq_id_next': nextq_id_next,
        'test': near_nodes
    }
    if request.session['path'] == 'start,f1,f2,f3,f4,f5,f6,f7,f8':
        return redirect('send_kad_num')
    else:
        return render(request, 'questions_yes_no.html', context)


def search(request):
    searched_items = request.GET.get('search', '')
    questions = Questions.objects.filter(quest_text__contains=searched_items)
    quest_text_edit = Questions.objects.filter(quest_id__contains=searched_items)
    print(quest_text_edit)
    context = {
        'search': searched_items,
        'questions': questions,
        'quest_text_edit': quest_text_edit,
        'test': GraphSelector.task,
    }

    return render(request, 'search.html', context)


def send_kad_num(request):
    error = ''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('congratulations')
        else:
            error = form.errors
    form = FeedbackForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'send_kad_num.html', context)


def json_Search(request):
    searched_items = request.GET.get('search', '')
    queryset = Questions.objects.filter(quest_text__contains=searched_items)
    questions = list(queryset.values('quest_id', 'quest_text'))
    return JsonResponse(questions, safe=False)

