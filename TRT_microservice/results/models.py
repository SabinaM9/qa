from django.db import models


class TestResults(models.Model):
    test_date = models.DateTimeField(auto_now=True, verbose_name='Date')
    squad = models.CharField(max_length=200, verbose_name='Squad')
    failed_tests = models.IntegerField(verbose_name='Failed Tests')
    # status = models.Choices(value='failed', names={"passed", "failed"})
    status = models.CharField(
        choices=[
            ("on", "passed"),
            ("of", "failed")
        ],
        verbose_name='Status',
        max_length=10
    )

    def __str__(self):
        return self.squad

    class Meta:
        verbose_name = "Test Result"
        verbose_name_plural = "Test Results"
