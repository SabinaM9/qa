from django.shortcuts import render
from .models import TestResults
from .forms import ResultForm


def main_page(request):
    results_list = TestResults.objects.all()
    return render(
        request,
        './index.html',
        {'results_list': results_list}
    )


def add_result(request):
    form = ResultForm()
    results_list = TestResults.objects.all()
    return render(
        request,
        './add_results.html',
        {'results_list': results_list, 'form': form}
    )


def thanks_page(request):
    squad = request.POST['squad']
    failed_tests = request.POST['failedTests']
    status = request.POST['status']

    result_to_add = TestResults(squad=squad, failed_tests=failed_tests, status=status)
    result_to_add.save()

    return render(
        request,
        './thanks_page.html',
        {
            'text': 'Test results were added successfully!',
            'squad': squad,
            'failed_tests': failed_tests,
            'status': status
        }
    )


def results(request):
    pass
    # totalDaysfailed
    # verdict: “unstable”, “stable”
    # lastFailureUnfixedDays: сколько дней последняя ошибка была непочиненной

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
