from django.contrib import admin
from django.urls import path, include
from results import views
from results.views import AddResultView, GetResultsView


app_name = 'results'
urlpatterns = [
    path('addTestResult/', AddResultView.as_view()),
    path('testResults/', GetResultsView.as_view())
]
