from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView, View
from django.views.generic.edit import FormMixin
from . import models, forms
from main.models import Question
from main.forms import QuestionForm


class MainPageView(CreateView, ListView):
    template_name = "main/index.html"
    model = models.Question
    success_url = "/"
    form_class = QuestionForm

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        context['form'] = QuestionForm()
        return context

    def get_queryset(self):
        return models.Question.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)


def completed(request):
    return render(request, "main/completed.html")


def renovation(request):
    return render(request, "main/renovation.html")


def projects(request):
    return render(request, "main/projects.html")


def house_construction(request):
    return render(request, "main/house_construction.html")


def extensions(request):
    return render(request, "main/extensions.html")
