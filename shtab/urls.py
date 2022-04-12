
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', PoruchenieView.as_view(), name = 'home'),
    path('poruchenie/id<int:por_pk>/', PoruchenieDetailView.as_view(), name = 'pordetaielview'),
    path('poruchenie/new/', NewPoruchenie.as_view(), name = 'newpor'),
    # path('authtorization/', LoginUserView().as_view(), name = 'authtorization'),
]
