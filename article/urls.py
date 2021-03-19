from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"


urlpatterns = [
    path('dashboard/',views.dashboarder,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('dashboard/article/<int:id>',views.detail,name = "detail"),
    path('dashboard/article/update/<int:id>',views.updateArticle,name = "update"),
    path('dashboard/article/delete/<int:id>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('comment/<int:id>',views.addcomment,name = "comment"),
    
    
]