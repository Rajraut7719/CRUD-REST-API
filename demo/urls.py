
from django.contrib import admin
from django.urls import path
from app import views
from app.views import StudentGeneric,StudentGeneric1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',StudentGeneric.as_view()),
    path('student/<id>',StudentGeneric1.as_view()),
]
