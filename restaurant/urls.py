"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.contrib.auth import views 
from django.conf import settings
from django.conf.urls.static import static

from restaurantapp.views import IndexView,  Restaurant_reg, feed_back, login_view, payment, view_res,view_restaurant,single_res

from restaurantapp import admin_urls, restaurant_urls





urlpatterns = [
    path('', IndexView.as_view()),
    path('res_reg', Restaurant_reg.as_view()),
    path('login', login_view.as_view()),
    path('payment', payment.as_view()),
    # path('res', view_res.as_view()),
    path('res', view_restaurant.as_view()),
    path('view', single_res.as_view()),
    path('feedback', feed_back.as_view()),

    


    path('admin/',admin_urls.urls()),
    path('restaurant/',restaurant_urls.urls()),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


