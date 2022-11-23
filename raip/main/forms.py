from django import forms

from main.models import HistoryUser, VKResult, Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'age', 'gender')


class CreatePredict(forms.ModelForm):
    class Meta:
        model = HistoryUser

        fields = ('patient', 'image')


class InputResult(forms.ModelForm):
    class Meta:
        model = VKResult

        exclude = ('patient',)
        fields = '__all__'
