import time

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TestResults
from .serializers import AddResultSerializer, ListResultSerializer


class AddResultView(generics.CreateAPIView):
    # class AddResultView(APIView):
    serializer_class = AddResultSerializer

    # {"squad": "My squad", "failed_tests": 2, "status": "passed"}
    # def post(self, request, format=None):
    #     squad = request.data.get('squad')
    #     failed_tests = request.data.get('failed_tests')
    #     status = request.data.get('status')
    #
    #     result_to_add = TestResults(squad=squad, failed_tests=failed_tests, status=status)
    #     result_to_add.save()
    #
    #     return Response(status=st.HTTP_201_CREATED)


class GetResultsView(generics.ListAPIView):
    # queryset = TestResults.objects.all()
    # def get(self, request):
    #     daysToFollow = request.data.get('daysToFollow')
    #     squad = request.data.get('squad')
    #     current_day = time.time()
    #     sql_request = 'SELECT test_date, sum(failedTests) as noffailures ' \
    #                   'GROUP BY test_date' \
    #                   f'HAVING squad = {squad} AND test_date > ({current_day} - {daysToFollow})'
    #     print(sql_request)
    #     return sql_request


    queryset = TestResults.objects.all()
    serializer_class = ListResultSerializer


    # def get(self, request):
    #     details = {...},  # “mm/dd/yyyy” : { status: ”b”, noffailrues: “y” }
    #     data_dict = {
    #         "details": details,
    #         "totalDaysfailed": ...,
    #         "verdict": ...,
    #         "lastFailureUnfixedDays": ...
    #     }
    #     return Response(data_dict, status=status.HTTP_200_OK)

    # def get(self, request):
    #     return Response({'some': 'data'})
    # serializer_class = ListResultSerializer
    # queryset = TestResults.objects.all()

    # def get(self, request, *args, **kwargs):

    # def get(self, request, format='json'):
    #     squad = request.data.get('squad')
    #     days_to_follow = request.data.get('daysToFollow:')
    #
    #     queryset = TestResults.objects.all()
    #
    #     # ЗДЕСЬ ЗАПРОС В БД
    #     return Response()


'''{ “details”: {
 “mm/dd1/yyyy” : { status: ”passed”, noffailrues: “0” }
 “mm/dd2/yyyy” : { status: ”passed”, noffailrues: “0” }
 “mm/dd3/yyyy” : { status: ”passed”, noffailrues: “0” }
 “mm/dd4/yyyy” : { status: ”failed”, noffailrues: “1” }
 “mm/dd5/yyyy” : { status: “pass”, noffailrues: “0” }
 “mm/dd6/yyyy” : { status: ”failed”, noffailrues: “1” }
 “mm/dd7/yyyy” : { status: ”failed”, noffailrues: “2” }

}
“totalDaysfailed”: “3”
“verdict”: “stable”
“las'''
