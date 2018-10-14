from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('hosp_no', 'atype', 'asource', 'age_grp', 'sex', 'drg', 'mdc', 'dx1',
        'px1', 'dyear', 'aqtr', 'dqtr', 'CCSDX', 'pdays', 'dstat')
