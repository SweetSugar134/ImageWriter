from django import forms


class MainForm(forms.Form):
    template_id = forms.IntegerField()
    text = forms.CharField()
    x = forms.IntegerField()
    y = forms.IntegerField()