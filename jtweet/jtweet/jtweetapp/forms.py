from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _



class JtweetUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("username",)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            get_user_model()._default_manager.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )




class JtweetUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(JtweetUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['followings'].queryset = self.fields['followings'].queryset.exclude(pk=self.instance.pk)
