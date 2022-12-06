from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.toLogin_view),
    path('login/', views.Login_view),
    path('toregister/', views.toregister_view),
    path('send/', views.Send_view),
    path('register/', views.register_view),
    path('login/index/', views.Index_view),
    path('login/detail/', views.Bookdetail_view),
    path('login/shopcar/', views.Shopcar_view),
    path('login/manager/', views.Manager_view),
    path('login/manager/shangjia/', views.Shangjia_view),
    path('login/manager/xiajia/', views.Xiajia_view),
    path('login/manager/xiugai/', views.Shangjia_view),
    path('login/manager/shouhou/', views.Shangjia_view),

    # path('shop/', include('shop.urls')),

]
# 设置静态文件路径
urlpatterns += staticfiles_urlpatterns()

