from django import forms


class Testform(forms.Form):
    testfield = forms.CharField(label='testfield', max_length=255)