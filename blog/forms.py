from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )


class ChkForm(forms.Form):
    labels = ['チェック', '複数チェック', 'ラジオボタン', '動的選択肢１', '動的選択肢２']
    SINGLE_CHOICE = [('1', 'OKなららチェック')]
    CHOICE = [
      ('1', '選択肢＜１＞'),
      ('2', '選択肢＜２＞'),
      ('3', '選択肢＜３＞')]

    one = forms.MultipleChoiceField(
        label=labels[0],
        required=False,
        disabled=False,
        initial=[],
        choices=SINGLE_CHOICE,
        widget=forms.CheckboxSelectMultiple(attrs={
          'id': 'one', 'class': 'form-check-input'}))

    two = forms.MultipleChoiceField(
        label=labels[1],
        required=False,
        disabled=False,
        initial=[],
        choices=CHOICE,
        widget=forms.CheckboxSelectMultiple(attrs={
          'id': 'two', 'class': 'form-check-input'}))

    four = forms.MultipleChoiceField(
        label=labels[3],
        required=False,
        disabled=False,
        widget=forms.CheckboxSelectMultiple(attrs={
          'id': 'four', 'class': 'form-check-input'}))

    three = forms.MultipleChoiceField(
        label=labels[2],
        required=False,
        disabled=False,
        initial=['2'],
        choices=CHOICE,
        widget=forms.RadioSelect(attrs={
          'id': 'three', 'class': 'form-check-input'}))

    five = forms.MultipleChoiceField(
        label=labels[4],
        required=False,
        disabled=False,
        widget=forms.RadioSelect(attrs={
          'id': 'five', 'class': 'form-check-input'}))


class Credits(forms.Form):
    lessons = (
        (10010010, "スタートアップセミナー", 1),
        (10110010, "総合英語Ｉａ", 2),
        (10110020, "総合英語Ｉｂ", 2),
    )

    startupseminar = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple()
    )
