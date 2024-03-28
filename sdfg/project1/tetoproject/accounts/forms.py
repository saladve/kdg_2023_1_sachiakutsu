from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
        ]

    def __init__(self, username=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        # ユーザーの更新前情報をフォームに挿入
        if username:
            self.fields['username'].widget.attrs['value'] = username

    def update(self, user):
        user.username = self.cleaned_data['username']
        user.save()
