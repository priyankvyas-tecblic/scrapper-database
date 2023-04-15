from django.urls import path,include
from scrapper_app import views
urlpatterns = [
    path('scrap/',views.ScrappingLinkedin.as_view()),
    path('dump/',views.DumpList.as_view()),
    
]