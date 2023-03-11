from django.urls import path
from . import views

urlpatterns = [
    path("accounts/", views.AccountsView.as_view()),
    path("accounts/balance/<int:idConta>", views.AccountBalanceView.as_view()),
]
