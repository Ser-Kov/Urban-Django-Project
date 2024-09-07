from django.contrib import admin
from django.urls import path
from task2.views import class_view, function_view
from task3.views import main_page, basket, shop
from task5.views import sign_up_by_html, sign_up_by_django


urlpatterns = [
    path('admin/', admin.site.urls),
    path('task2/func_view', function_view),
    path('task2/class_view', class_view),
    path('task3/main', main_page),
    path('task3/basket', basket),
    path('task3/shop', shop),
    path('logging/temp', sign_up_by_html),
    path('logging/form', sign_up_by_django)
]
