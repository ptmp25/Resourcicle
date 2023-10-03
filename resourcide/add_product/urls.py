from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.first_step, name='first_step'),
    path('add_product/step1/', views.first_step, name='first_step'),
    path('add_product/step2/', views.second_step, name='second_step'),
    path('add_product/step3/', views.third_step, name='third_step'),
    path('add_product/step4/', views.fourth_step, name='fourth_step')
]