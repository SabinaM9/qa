from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TestResults(models.Model):
    test_date = models.DateTimeField(auto_now=True, verbose_name='date')
    squad = models.CharField(max_length=200, verbose_name='squad', blank=False)
    failed_tests = models.IntegerField(verbose_name='failedTests', blank=False,
                                       validators=[MinValueValidator(0), MaxValueValidator(100000)])
    status = models.CharField(
        choices=[
            ("on", "passed"),
            ("of", "failed")
        ],
        verbose_name='Status',
        max_length=10, blank=False
    )
    #
    # def __str__(self):
    #     return self.squad
    #
    # class Meta:
    #     verbose_name = "Test Result"
    #     verbose_name_plural = "Test Results"
