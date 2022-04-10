from django.urls import path
from results.views import AddResultView, GetResultsView


app_name = 'results'
urlpatterns = [
    path('addTestResult/', AddResultView.as_view()),
    path('testResults', GetResultsView.as_view())
]
