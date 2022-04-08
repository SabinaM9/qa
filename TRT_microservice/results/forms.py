from django import forms


class ResultForm(forms.Form):
    squad = forms.CharField(max_length=200, required=True)
    failedTests = forms.IntegerField(min_value=0, max_value=100000, required=True)
    status = forms.ChoiceField(required=True, choices=[("on", "passed"), ("of", "failed")])
