from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('root', include('rootapp.urls')),
    path('admin/', admin.site.urls),
    path('', include('calculatorapp.urls'))
]
