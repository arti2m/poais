from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models.Poruchenie import *

from .utils import DataMixin
from .forms import *


# class LoginUserView(DataMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'shtab/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_(**kwargs)
#         c_def = self.get_user_context(title = 'АИС | Авторизация')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('   home')

class PoruchenieView(DataMixin, ListView):
    model = Poruchenie
    template_name = 'shtab/index.html'
    context_object_name = 'pors'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'АИС | Поручения')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        # return Poruchenie.object.filter(otvotpo = User)
        return Poruchenie.objects.all()


class PoruchenieDetailView(DataMixin, DetailView):
    model = Poruchenie
    template_name = 'shtab/pordetailview.html'
    pk_url_kwarg = 'por_pk'
    context_object_name = 'por'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'АИС | Поручения')
        return dict(list(context.items()) + list(c_def.items()))

class NewPoruchenie(DataMixin,CreateView):
    form_class = NewPoruchenieForm
    template_name = 'shtab/newpor.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'АИС | Поручения')
        return dict(list(context.items()) + list(c_def.items()))


# class PoruchenieOtv(DataMixin, ListView):
#     model = Poruchenie
#     template_name = 'shtab/index.html'
#     context_object_name = 'pors'
#     allow_empty = False
#
#     def get_queryset(self):
#         return Poruchenie.objects.filter(cat__pk=self.kwargs['cat_slug'], is_published=True)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Категория - ' + str(context['pors'][0].cat),
#                                       cat_selected=context['pors'][0].cat_id)
#         return dict(list(context.items()) + list(c_def.items()))