from django.urls import path

from menu.views import IndexProgectView


app_name = 'menu'

urlpatterns = [
    path('menu/', IndexProgectView.as_view(), name='index')
]
