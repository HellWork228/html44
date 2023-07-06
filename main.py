from flask import Flask
import random

facts_list= [
    'Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.',
    'Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.',
    'Один из способов борьбы с технологической зависимостью - это поиск занятий, которые приносят удовольствие и улучшают настроение.',
]
app = Flask(__name__)

@app.route("/random_fact")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'
@app.route("/")
def random_fact():
    return f'<h1>привет, это мой сайт, жми чтобы получить интересный факт</h1>  <a href="/random_fact">Посмотреть случайный факт!</a>'
@app.route("/secret")
def hihi():
    return f'<h1>LoL! ты попал на секретную страницу</h1> <p>смотри, это эл. Можешь послушать музыку пока восхищаешься им</p> <img src="https://slovnet.ru/wp-content/uploads/2018/12/2-9.png" alt="Image 1"> <script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script><div class="elfsight-app-6e39afef-42fd-4db8-af48-204c510b0d4b"></div>' 

app.run()
