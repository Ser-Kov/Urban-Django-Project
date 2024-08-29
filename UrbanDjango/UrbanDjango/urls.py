from django.contrib import admin
from django.urls import path
from task4.views import main_page, shop, basket


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_page),
    path('shop/', shop),
    path('basket/', basket)
]
