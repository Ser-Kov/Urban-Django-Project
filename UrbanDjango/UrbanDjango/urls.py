from django.contrib import admin
from django.urls import path
from task2.views import function_view, class_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('function-view/', function_view, name='function_view'),
    path('class-view/', class_view, name='class_view')
]
