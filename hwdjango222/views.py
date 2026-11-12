import datetime
import random

from django.http import HttpResponse


def home(request):
    days = [
        "Понеділок",
        "Вівторок",
        "Середа",
        "Четвер",
        "П'ятниця",
        "Субота",
        "Неділя"
    ]

    quotes = [
        "Навчання — це скарб, який завжди з тобою.",
        "Успіх приходить до тих, хто працює.",
        "Кожен день — це нова можливість.",
        "Ніколи не пізно вчитися чомусь новому.",
        "Маленькі кроки ведуть до великих результатів."
    ]

    today = days[datetime.datetime.today().weekday()]
    quote = random.choice(quotes)

    html = f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Головна сторінка</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <h2>Сьогодні: {today}</h2>
            <p>Цитата дня: {quote}</p>
        </body>
    </html>
    """

    return HttpResponse(html)