from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q 

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')
    model = Post

class ListPostView(ListView):
    template_name = 'teto/teto_list.html'
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'teto/teto_create.html'
    model = Post
    fields = ('title', 'music', 'text', 'link', 'category')
    success_url = reverse_lazy('postlist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super() .form_valid(form)

class DetailPostView(LoginRequiredMixin, DetailView):
    template_name = 'teto/teto_detail.html'
    model = Post

class DeletePostView(LoginRequiredMixin, DeleteView):
    template_name = 'teto/teto_confirm_delete.html'
    model = Post
    success_url = reverse_lazy('postlist')

    def get_object(self, queryset=None):
        obj = super() .get_object(queryset)

        if obj.user != self.request.user:
            raise PermissionDenied
        return obj

def index_view(request):
    object_list = Post.objects.order_by('-id')
    return render(request, 'teto/index.html', {})

class CreateCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('post', 'text')
    template_name = 'teto/comment_form.html'

    def get_context_data(self, **kwargs):
        context = super() .get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super() .form_valid(form)

    def get_success_url(self):
        return reverse('postdetail', kwargs={'pk': self.object.post.id})


