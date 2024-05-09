
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #user end point start
    path('api/user/',include('user.urls')),
    
    #product end point start
    path('api/product/',include('products.urls'))
]
