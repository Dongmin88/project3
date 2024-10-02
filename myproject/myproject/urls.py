"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomLoginCancelledView
from django.shortcuts import redirect

def login_cancelled(request):
    return redirect('/login')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', views.hello_world, name='hello_world'),
    path('accounts/social/login/cancelled/', CustomLoginCancelledView.as_view(), name='socialaccount_login_cancelled'),
    path('accounts/3rdparty/login/cancelled/', login_cancelled, name='socialaccount_3rdparty_login_cancelled'),  # 이 줄을 추가하여 해당 경로에서 메인 페이지로 리디렉션
    path('', views.main_page, name='main_page'),  # 메인 페이지
    path('login/', views.login_page, name='login_page'),  # 로그인 페이지
    path('feature1/', views.feature_page1, name='feature_page1'),  # 기능 페이지 1
    path('feature2/', views.feature_page2, name='feature_page2'),  # 기능 페이지 2
    path('accounts/', include('allauth.urls')),  # allauth URL 추가

]
