from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('all/', views.ProfileView.as_view()),
    path('all/<int:pk>/', views.ProfileView.as_view()),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)