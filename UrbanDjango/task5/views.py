from django.shortcuts import render, HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['Maxim', 'Alex', 'Oleg']
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username in users:
            error = 'Пользователь уже существует'
            info['error'] = error
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        elif password != repeat_password:
            error = 'Пароли не совпадают'
            info['error'] = error
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        elif int(age) < 18:
            error = 'Вы должны быть старше 18'
            info['error'] = error
            for key, value in info.items():
                if value == error:
                    return HttpResponse(f'{key}: {value}')
        else:
            return HttpResponse(f'Приветствуем, {username}!')
    return render(request, 'fifth_task/registration_page_template.html')


def sign_up_by_django(request):
    users = ['Maxim', 'Alex', 'Oleg']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                error = 'Пользователь уже существует'
                info['error'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            elif password != repeat_password:
                error = 'Пароли не совпадают'
                info['error'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            elif age < 18:
                error = 'Вы должны быть старше 18'
                info['error'] = error
                for key, value in info.items():
                    if value == error:
                        return HttpResponse(f'{key}: {value}')
            else:
                return HttpResponse(f'Приветствуем, {username}!')
    else:
        form = UserRegister()
        return render(request, 'fifth_task/registration_page_form.html', {'form': form})
