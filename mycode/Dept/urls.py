from django.urls import path

from . import views

app_name = 'Dept'

urlpatterns = [
    #path('', views.index, name='index'),
    path('ft/', views.ft_index, name='ft_index'),
    path('ft/<int:ft_id>/', views.testdetail, name='detail'),
    path('ft/calls/<int:call_id>/', views.business_call, name='business_call'),
    path('ft/ttff/<int:tf_id>/', views.ttff_detail, name='ttff_detail'),#所有的name都要和view以及html的名字一样
    path('ft/ss/<int:ss_id>/', views.business_ss, name='business_ss'),
]

