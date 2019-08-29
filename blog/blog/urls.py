from django.contrib import admin
from django.urls import path
import task.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',task.views.index,name='index'),
    path('create/',task.views.create,name='create'),
    path('read/<int:post_id>',task.views.read,name='read'),
    path('update/<int:post_id>',task.views.update,name='update'),
    path('delete/<int:post_id>',task.views.delete,name='delete'),
    path('signup/',accounts.views.signup,name='signup'),
    path('login/',accounts.views.login,name='login'),
    path('logout/',accounts.views.logout, name='logout'),
    path('c_create/<int:post_id>',task.views.c_create,name='c_create'),
]
