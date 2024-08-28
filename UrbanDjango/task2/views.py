from django.shortcuts import render


def function_view(request):
    return render(request, 'second_task/function_template.html')


def class_view(request):
    return render(request, 'second_task/class_template.html')
