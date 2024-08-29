from django.shortcuts import render


def main_page(request):
    title = 'Мой сайт'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/menu.html', context)


def shop(request):
    title = 'Магазин'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'title': title,
        'games': games
    }
    return render(request, 'fourth_task/shop.html', context)


def basket(request):
    title = 'Корзина'
    context = {'title': title}
    return render(request, 'fourth_task/basket.html', context)
