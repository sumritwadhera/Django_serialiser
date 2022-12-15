"""opsec_project URL Configuration

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
from django.urls import path

from opsec_app.views import S3, Lambda2,cost3,ITYPE,USTYPE,REG,USAGE,REG_OT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Lambda2', Lambda2.as_view()),
    path('S3', S3.as_view()),
    path('cost3', cost3.as_view()),
    path('ITYPE', ITYPE.as_view()),
    path('USTYPE', USTYPE.as_view()),
    path('REG', REG.as_view()),
    path('USAGE', USAGE.as_view()),
    path('REG_OT', REG_OT.as_view()),

]
