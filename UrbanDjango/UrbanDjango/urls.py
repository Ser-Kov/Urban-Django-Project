from django.contrib import admin
from django.urls import path
from task2.views import function_view, class_view
from task3.views import main_page, shop, basket


urlpatterns = [
    path('admin/', admin.site.urls),
    path('function-view/', function_view),
    path('class-view/', class_view),
    path('main/', main_page),
    path('shop/', shop),
    path('basket/', basket)
]
