# Проект Интерактивный помощник
Проект подготовлен в рамках прохождения обучения по курсу в IT университете по программе **"Веб-разработка с Python: Django framework"** (на базе ПГНИУ).  

**Решаемая проблема:**  
В процессе проведения проверок в части соблюдения земельного законодательства, гражданами, а также кадастровыми инженерами, нередко допускаются ошибки, которые можно назвать типовыми.  
Каждому такому нарушению присущи некоторые признаки.  
Совокупность нескольких признаков может в явной мере свидетельствовать о наличии нарушения.  
Таким образом, для того, чтобы формализовать процесс выявления типовых нарушений, web-сервис может задавать наводящие вопросы (подразумевающие в качестве ответа «Да» или «Нет») тестируемым и, в случае, если в процессе опроса были выявлены признаки, характеризующие нарушение, показать испытуемому сообщение о наличии нарушения, а также рекомендацию по его устранению  
В случае отсутствия нарушений, тестируемому будет предложено ввести кадастровый номер объекта для включения его в в дальнейшем в перечень объектов не имеющих нарушения.  

Принцип перемещения между вопросами основан на Графах  

Разработанное Web-приложение позволяет наполнить базу данных вопросами (которые будут являться вершинами графа) и односложными ответами на эти вопросы (да или нет, которые будут являться рёбрами графа)  
Для обеспечения связности вершин используется дополнительная таблица, описывающая рёбра графа (граф является направленным, путь указывается через запятую (откуда и куда мы можем перейти), также указывается маркер графа (ответ yes/no))

  
## Ознакомиться с промышленной (доработанной) версией приложения вы можете по ссылке.  
https://zpol.permkrai.ru  
Тестовые данные:  
Кадастровый номер: 59:00:0000000:123  
Почта: test@mail.ru
