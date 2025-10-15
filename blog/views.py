from django.shortcuts import render, get_object_or_404
from site_setup.models import SiteSetup

# Create your views here.

def index(request):
    return render(
        request,
        'blog/pages/index.html',
    )