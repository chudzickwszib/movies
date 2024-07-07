from django import forms
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator, MinLengthValidator
from django.forms.utils import ErrorList


class MovieForm(forms.Form):
    tmdb_id = forms.CharField(max_length=255, label='Tmdb ID',
                              validators=[
                                  RegexValidator(r'tt\d{7}', message='Proszę podać poprawny TMDB ID')
                              ],
                              error_messages={
                                  'invalid': 'Proszę podać TMDB ID w formacie tt123456789'
                              })
    original_title = forms.CharField(label='Tytuł filmu', max_length=1000,
                                     validators=[MinLengthValidator(3)])
    overview = forms.CharField(label='Opis filmu', validators=[MinLengthValidator(10)],
                               widget=forms.Textarea(attrs={'rows': 3}))
    release_date = forms.DateField(label='Data wydania filmu',
                                   widget=forms.DateInput(attrs={'type': 'date'}))
    cast = forms.CharField(label='Obsada', max_length=1000)
    genres = forms.CharField(label='Gatunki filmu', max_length=1000)
    keywords = forms.CharField(label='Słowa kluczowe')
    director = forms.CharField(label='Reżyser', max_length=1000)

    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        for visible_field in self.visible_fields():
            visible_field.field.widget.attrs['class'] = 'uk-input uk-margin-small-bottom'
