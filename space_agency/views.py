from django.shortcuts import render
from django.views.generic import ListView
from .models import Slider


class LendingListView(ListView):
    """
    Представление для отображения списка объектов модели Slider на главной странице.
    """
    
    model = Slider
    template_name = 'index.html'
    context_object_name = 'slider'
