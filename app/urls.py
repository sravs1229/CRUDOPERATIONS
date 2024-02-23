from django.urls import path

from app import views


urlpatterns = [
    path('',views.index),
    path('about',views.about,name="about"),
    path('insert',views.insertdata,name="insert"),
    path('update/<id>',views.update,name="update"),
    path('delete/<id>',views.delete,name="delete")
]
