from django.db import models
import networkx as nx


class Questions(models.Model):
    quest_id = models.CharField('Идентификатор вопроса', max_length=30)
    quest_text = models.TextField('Текст вопроса')
    quest_comment = models.TextField('Текст подсказки', blank=True)

    def __str__(self):
        return self.quest_text

    # def text(self):
    #     return self.quest_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Feedback(models.Model):
    feedback_email = models.EmailField('E-mail', max_length=30, blank=True)
    feedback_kad_num = models.CharField('Кадастровый номер', max_length=20)

    def __str__(self):
        return self.feedback_kad_num

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class Graph(models.Model):
    graph_path_id = models.CharField('Идентификаторы ответов (откуда куда) пр: q1,q2', max_length=20)
    graph_q_id = models.CharField('Ответ yes или no', max_length=3)

    def __str__(self):
        return self.graph_path_id

    def ans(self):
        return self.graph_q_id

    class Meta:
        verbose_name = 'Граф соответствий'
        verbose_name_plural = 'Граф соответствий'

# class Result(models.Model):
#     result_id = models.CharField('Идентификатор ответа', max_length=10)
#     result_text = models.TextField('Рекомендация')
#
#     def __str__(self):
#         return self.result_text
#
#     class Meta:
#         verbose_name = 'Рекомендация'
#         verbose_name_plural = 'Рекомендации'


class GraphSelector:
    G = nx.MultiDiGraph()
    start_pos = 'start'
    nodes = []
    paths = []
    task = Questions.objects.filter(quest_id=start_pos)
    # Собираем вершины графа
    for node in Questions.objects.all().values_list('quest_id', flat=True):
        nodes.append(node)
    # Загружаем вершины в граф
    G.add_nodes_from(list(set(nodes)))
    # Собираем рёбра графа
    for path in Graph.objects.all().values_list('graph_path_id', flat=True):
        paths.append(path)
        # Загружаем рёбра в граф
        G.add_edge(path.split(',')[0], path.split(',')[1], key=Graph.graph_q_id)
    for node in list(Graph.objects.all()):
        # Вытаскиваем из базы маркер ребра
        answer = Graph.ans(node)
        # Вытаскваем из базы точки рёбер, разделяем и добавляем в граф
        G.add_edge(str(node).split(',')[0], str(node).split(',')[1], key=answer)
