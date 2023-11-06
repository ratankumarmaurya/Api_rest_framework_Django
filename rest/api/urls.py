from .views import StudentsView
from django.urls import path

urlpatterns = [
    path('basic/', StudentsView.as_view()),
    path('basic/<int:id>/', StudentsView.as_view())
]
