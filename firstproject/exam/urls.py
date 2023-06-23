from django.urls import path
from exam import views
urlpatterns = [
    path('testpaper',views.testpaper),
    path('examresult',views.examresult),
]
