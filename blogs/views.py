from django.shortcuts import render, redirects, get_object_or_404
from .models import Blog
from .forms import BlogForm

def index(request):
    blogs = Blog.objects.order_by("-created_datetime")
    return render(request, 'blogs/index.html', {"blogs": blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogs/detail.html', {"blog": blog})

def new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            form = BlogForm
        return render(request, 'blogs/new.html', {'form': form})