from django.shortcuts import render


def main_page(request):
    title = 'Мой сайт'
    h1_text = 'Главная страница'
    text_main = 'Главная'
    text_shop = 'Магазин'
    text_basket = 'Корзина'
    context = {
        'title': title,
        'h1_text': h1_text,
        'text_main': text_main,
        'text_shop': text_shop,
        'text_basket': text_basket
    }
    return render(request, 'third_task/main_page.html', context)


def shop(request):
    title = 'Магазин'
    product1 = 'Atomic Heart'
    product2 = 'Cyberpunk 2077'
    product3 = 'PayDay 2'
    context = {
        'title': title,
        'product1': product1,
        'product2': product2,
        'product3': product3
    }
    return render(request, 'third_task/shop.html', context)


def basket(request):
    title = 'Корзина'
    context = {'title': title}
    return render(request, 'third_task/basket.html', context)