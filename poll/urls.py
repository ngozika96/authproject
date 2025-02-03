from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authapp.urls"))
]


urlpatterns = [
    path('welcome to the pollapp/', views.say_welcome to the pollapp)
]

