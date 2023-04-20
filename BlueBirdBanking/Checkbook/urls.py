from django.urls import path
from .import views

urlpatterns= [
    # Sets the url path to the home page index.html
    path('', views.home, name='index'),

    # Sets the url path to create new account page createnewaccount.hmtl
    path('create/', views.create_account, name='create'),


    path('<int:pk>/balance/', views.balance, name='balance'),


    path('transaction/', views.transaction, name='transaction')
]