from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
    template_name = "list/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class RegisterPage(FormView):
    template_name = "list/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwrgs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterPage, self).get(*args, **kwrgs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__startswith=search_input)
        context["search_input"] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"
    template_name = "list/details.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        "title",
        "description",
        "complete",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(TaskCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy("tasks")


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = [
        "title",
        "description",
        "complete",
    ]
    success_url = reverse_lazy("tasks")


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "list/delete_task.html"
    success_url = reverse_lazy("tasks")
