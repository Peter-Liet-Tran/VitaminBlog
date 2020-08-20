from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vitamin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView,
        )


class UserVitaminListView(ListView):
    model = Vitamin
    template_name = 'vitamin_tracker/user_vitamins.html' # <app>/<model>_<viewtype>.html

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        user = self.request.user
        vitamins = Vitamin.objects.filter(author=user)
        total = 0

        for vita in vitamins:
            total += vita.price


        context['vitamins'] = vitamins
        context['total'] = total

        return context

    def get_queryset(self):
        user = self.request.user
        return Vitamin.objects.filter(author=user)

class VitaminDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Vitamin 
    success_url = '/user/'

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

