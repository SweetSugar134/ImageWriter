from django import forms


class MainForm(forms.Form):
    template_id = forms.IntegerField(widget=forms.NumberInput(attrs={'value': '1'}))
    text = forms.CharField()
    x = forms.IntegerField()
    y = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'image', 'src': 'https://i.pinimg.com/736x/0b/6f/aa/0b6faa695924bb5464ec043782ba6d7f.jpg'}))