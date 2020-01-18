from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from taggit.models import Tag

from .models import JobPost
from .forms import JobPostForm


def index(request, tag_slug = None):
    posts = JobPost.objects.order_by('-date_posted')

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    context = {'posts': posts, 'tag': tag}
    return render
    (request, 'jobs/home.html', context)


class AddEntryView(CreateView):
    model = JobPost
    form_class = JobPostForm
    template_name = 'jobs/addJobPost.html'
    success_url = reverse_lazy('home')
