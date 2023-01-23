from django.urls import path, include
from .views import Province_View


urlpatterns = [
    path('provincia', Province_View.as_view())
]