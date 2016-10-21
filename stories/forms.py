from django import forms
from .models import Story, Themes, Reading, Reader
from django_select2.forms import  Select2Widget
from django.utils import timezone
from datetimewidget.widgets import DateWidget
import select2.fields


class StoryForm(forms.ModelForm):
    pubdate = forms.DateField(widget=forms.SelectDateWidget)

    
    class Meta:
        model = Story
        fields = ['title', 'author', 'type', 'pubdate', 'suggested_by', 'themes', 'image']
        # widgets = {
        #     'themes': Select2Widget,
        # }


class ReadingForm(forms.ModelForm):
    date = forms.DateField(label="", widget=DateWidget(bootstrap_version=3), initial=timezone.now())
    event = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Event"}))
    # reader = forms.ModelChoiceField(queryset=Reader.objects.all(),label="", widget=Select2Widget, empty_label=None)
    # story = forms.ModelChoiceField(queryset=Story.objects.all(), label="", widget=Select2Widget, empty_label=None)
    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(ReadingForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['story'].widget = HiddenInput()

    class Meta:
        model = Reading

        fields = (
            'event',
            'reader',
            'story',
            'date'
        )
        # widgets = {
        #     'reader': Select2Widget,
        #     'story': Select2Widget,
        #     # 'date': DateWidget(attrs={'id': "id_date"}, usel10n=True, bootstrap_version=3)
        # }


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'email', 'phone']


