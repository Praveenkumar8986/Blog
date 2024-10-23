from django.shortcuts import render,get_object_or_404
from blog.models import post
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def post_list_view(request):
    post_list=post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,"blog/post_detail.html",{'post':post})


import os
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # Construct the path to the file
    file_path = os.path.join(BASE_DIR, 'build', 'build\index.html')  # Adjust path if necessary
    print(file_path)
    # Open the file in read mode and return its content as an HttpResponse
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    return HttpResponse(file_content, content_type='text/html')

    