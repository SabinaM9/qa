import datetime

from django.core.exceptions import BadRequest
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
    def get(self, request):
        try:
            squad_to_get = request.query_params.get('squad')
            days_to_get = int(request.query_params.get('daysToFollow'))
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
            if len(db_data.filter(noffailures=0)) and db_data.order_by('-test_date')[:1][0]["noffailures"] != 0:  # if we have even 1 date passed
                last_failures = []
                for obj in db_data.order_by('-test_date'):
                    if obj['noffailures'] > 0:
                        last_failures.append(obj['test_date'])
                    else:
                        break
                lastFailureUnfixedDays = (today - last_failures.sort()[0]).days
        except Exception:
            raise BadRequest("Invalid request. Please enter required parameters: 'squad', 'daysToFollow'")

        return Response(
            {
                "details": details,
                "totalDaysfailed": totalDaysfailed,
                "verdict": verdict,
                "lastFailureUnfixedDays": lastFailureUnfixedDays
            }
        )
