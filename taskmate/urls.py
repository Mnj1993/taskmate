from django.contrib import admin
from django.urls import path , include
from todolist_app import views as todolist_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name='index'),
    path('todolist/', include('todolist_app.url')), # 6) i made
    path('account/', include('users_app.urls')),
    path('contact', todolist_views.contact, name='contact'), # 10) i made
    path('about', todolist_views.about, name='about'),# 10) i made
    #path('task/', include('todolist_app.url')) # 1) i made, then create url.py in todolist
]
