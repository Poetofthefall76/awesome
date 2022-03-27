from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.views.generic import CreateView, ListView, TemplateView, View
from django.views.generic.edit import FormMixin
from . import models, forms
from main.models import Question
from main.forms import QuestionForm


class MainPageView(CreateView, ListView):
    template_name = "main/awesome.html"
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


class Image(ListView):
    model = models.Image

    def get_queryset(self):
        return models.Image.objects.all()
