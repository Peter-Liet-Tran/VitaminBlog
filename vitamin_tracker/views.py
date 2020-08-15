from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vitamin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )

class UserVitaminListView(ListView):
    model = Vitamin
    template_name = 'vitamin_tracker/user_vitamins.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'vitamins'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Vitamin.objects.filter(author=user)

class VitaminDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Vitamin 
    success_url = '/'

    def test_func(self): #Makes sure it is the author updating the post
        vitamin = self.get_object()
        if self.request.user == vitamin.author:
            return True
        return False

class VitaminDetailView(DetailView):
    model = Vitamin

class VitaminCreateView(LoginRequiredMixin, CreateView):
    model = Vitamin
    fields = ['title', 'price', 'url', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        vitamin = form.save(commit=False)
        #post.instance.author = self.request.user
        vitamin.save()
        #form.instance.author = self.request.user
        return super().form_valid(form)


class VitaminUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Vitamin
    fields = ['title', 'price', 'url', 'image']
    
    def form_valid(self, form): #Saves logged in user as author
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #Makes sure it is the author updating the post
        vitamin = self.get_object()
        if self.request.user == vitamin.author:
            return True
        return False

