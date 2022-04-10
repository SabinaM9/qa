import datetime

from django.db.models import Sum
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TestResults
from .serializers import AddResultSerializer


class AddResultView(generics.CreateAPIView):
    serializer_class = AddResultSerializer


class GetResultsView(APIView):

    # http://127.0.0.1:8000/testResults?squad=testtest&daysToFollow=2
    def get(self):
        squad_to_get = self.request.query_params.get('squad')
        days_to_get = int(self.request.query_params.get('daysToFollow'))
        today = datetime.date.today()
        needed_date = today - datetime.timedelta(days=days_to_get)

        db_data = TestResults.objects\
            .values('test_date')\
            .annotate(noffailures=Sum('failed_tests'))\
            .filter(squad__iexact=squad_to_get, test_date__gte=needed_date)
        # SELECT date, sum(failed_tests) from table GROUP BY date HAVING squad = <squad_to_get> AND date > <needed_date>

        details = {
            str(obj["test_date"]): {"status": "passed" if not obj["noffailures"] else "failed",
                                    "noffailures": obj["noffailures"]}
            for obj in db_data
        }
        totalDays = sum((1 for _ in details))
        totalDaysfailed = sum((1 if test_data["noffailures"] else 0 for test_data in details.values()))
        verdict = "stable" if 1 < totalDaysfailed / totalDays < 0.10 else "unstable"
        lastFailureUnfixedDays = 0

        if db_data.order_by('-test_date')[:1][0]["noffailures"] != 0:
            last_failure_day = db_data.values('test_date').filter(failed_tests__gte=0).order_by('-test_date')[:1][0]
            lastFailureUnfixedDays = (today - last_failure_day['test_date']).days

        return Response(
            {
                "details": details,
                "totalDaysfailed": totalDaysfailed,
                "verdict": verdict,
                "lastFailureUnfixedDays": lastFailureUnfixedDays
            }
        )
