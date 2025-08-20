from django.urls import path,re_path 
from ShuaBu import views # 从自己的 app 目录引入 views 
urlpatterns = [ 
    path('', views.main),
    path('test/', views.add_log),
] 