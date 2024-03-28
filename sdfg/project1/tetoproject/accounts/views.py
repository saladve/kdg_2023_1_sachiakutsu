from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignupForm, UserChangeForm

class Signupview(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'accounts/change.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        #formのupdateメソッドにログインユーザーを渡して更新
        form.update(user=self.request.user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # 更新前のユーザー情報をkwargsとして渡す
        kwargs.update({
            'username' : self.request.user.username,
        })
        return kwargs