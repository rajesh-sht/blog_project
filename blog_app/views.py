from django.shortcuts import redirect, render
from blog_app.models import Post
from django.contrib.auth.decorators import login_required
from blog_app.forms import PostForm
from django.utils import timezone


def post_list(request):
    # use filter if want multiple records = QuerySet => ORM
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    return render(request, 'post_list.html', {"posts": posts})


def post_detail(request, id):
    # use get if want only one record
    post = Post.objects.get(pk=id)
    return render(request, 'post_detail.html', {'post': post})


@login_required
def draft_list(request):
    # use filter if want multiple records = QuerySet => ORM
    posts = Post.objects.filter(
        published_at__isnull=True).order_by('-published_at')
    return render(request, 'post_list.html', {"posts": posts})


@login_required
def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("draft-list")

    return render(request, 'post_create.html', {"form": form})


@login_required
def post_publish(request, id):
    post = Post.objects.get(pk=id)
    post.published_at = timezone.now()
    post.save()
    return redirect('post-list')


@login_required
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post-list')


@login_required
def post_update(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('post-list')
    else:
        form = PostForm(instance=post)
        return render(request, 'post_create.html', {'form': form})
