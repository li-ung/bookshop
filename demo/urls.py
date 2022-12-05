from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.toLogin_view),
    path('login/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('send/', views.Send_view),
    path('register/', views.register_view),
    path('login/index/', views.Index_view),
    path('login/index/shopcar/', views.Shopcar_view),
    path('login/index/manager/', views.Manager_view),
    path('login/index/manager/shangjia/', views.Shangjia_view),
    path('login/index/manager/xiajia/', views.Xiajia_view),
    path('login/index/manager/xiugai/', views.Shangjia_view),
    path('login/index/manager/shouhou/', views.Shangjia_view),


    # path('shop/', include('shop.urls')),

]
