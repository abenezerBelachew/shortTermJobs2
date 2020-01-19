from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
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
    return render(request, 'jobs/home.html', context)


class AddEntryView(LoginRequiredMixin, CreateView):
    model = JobPost
    form_class = JobPostForm
    template_name = 'jobs/addJobPost.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.employer = self.request.user
        return super().form_valid(form)

def addJobPost(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)

        if form.is_valid():
            jobPost = form.save(commit=False)
            jobPost.employer = request.user
            jobPost.save()
            return redirect('home')
    else:
        form = JobPostForm()
    context = {'form': form, 'employer': request.user}
    return render(request, 'jobs/addJobPost.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', 
        {'form': form})
