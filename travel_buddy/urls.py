"""travel_buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from apps.login_reg_app.models import User as User
from apps.travels_app.models import Trip as Trip

class UserAdmin(admin.ModelAdmin):
  pass
admin.site.register(User, UserAdmin)

class TripAdmin(admin.ModelAdmin):
    pass
admin.site.register(Trip, TripAdmin)
# class FruitAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Fruit, FruitAdmin)
#
# class DonutAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Donut, DonutAdmin)
#
# class GroupAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(Group, GroupAdmin)




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.default_app.urls', namespace='default')),
    url(r'^main/', include('apps.login_reg_app.urls', namespace='users')),
    url(r'^travels/', include('apps.travels_app.urls', namespace='travels')),
]
