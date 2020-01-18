from django.forms import ModelForm
from .models import JobPost

class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description',
                'photo', 'pay', 'tags']