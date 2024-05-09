
from django.urls import path
from .views import signUP,signIn


urlpatterns = [
    path('signup',signUP.as_view()),
    path('signin',signIn.as_view()),
]
