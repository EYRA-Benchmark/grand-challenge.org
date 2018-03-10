from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import BLANK_CHOICE_DASH
from django.utils.translation import gettext

from comicmodels.models import Page


class PageCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        challenge_name = kwargs.pop('challenge_short_name', None)
        self.challenge_pk = kwargs.pop('challenge_pk', None)

        super().__init__(*args, **kwargs)

        if challenge_name is not None and 'html' in self.fields:
            self.fields['html'].widget.config['comicsite'] = challenge_name

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'Save'))

    def clean_title(self):
        """ Ensure that page titles are not duplicated for a challenge """
        title = self.cleaned_data['title']

        queryset = Page.objects.filter(comicsite__pk=self.challenge_pk,
                               title=title)

        if self.instance is not None:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise ValidationError(
                gettext(
                    'A page with that title already exists for this challenge'
                ),
                code='duplicate',
            )

        return title

    class Meta:
        model = Page
        fields = ('title', 'permission_lvl', 'display_title', 'hidden', 'html')


class PageUpdateForm(PageCreateForm):
    """ Like the page update form but you can also move the page """
    move = forms.CharField(widget=forms.Select)
    move.required = False
    move.widget.choices = (
        (BLANK_CHOICE_DASH[0]),
        (Page.FIRST, 'First'),
        (Page.UP, 'Up'),
        (Page.DOWN, 'Down'),
        (Page.LAST, 'Last'),
    )
