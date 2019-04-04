from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import logging

#@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    logger=logging.getLogger('command')
    logger.info('django')

#@login_required
def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

#@login_required
def post_category_programming(request):
   posts=Post.objects.filter(category__contains="プログラミング").order_by('-published_date')
   return render(request, 'blog/post_list.html', {'posts': posts})

#@login_required
def post_category_cooking(request):
   posts=Post.objects.filter(category__contains="料理").order_by('-published_date')
   return render(request, 'blog/post_list.html', {'posts': posts})

#@login_required
def post_aboutme(request):
   return render(request, 'blog/about_me.html', {})

"""
@login_required #写真投稿機能をつける前までに動いていたpost_new
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'blog/post_detail.html', {'post':post})
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

"""

@login_required
def post_new(request):
    #global post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            form.save()
            #return redirect('post_detail', pk=post.pk) redirectは別のurlに飛ばす return renderはレスポンスを返す(何かを送る)
            return render(request, 'blog/post_detail.html', {'post':post})
    else:
        form =PostForm()
        post = Post.objects.all()

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'post': post
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return render(request, 'blog/post_detail.html', {'post':post})
            #return redirect('post_detail', pk=post.pk)
    else:
        form =PostForm(instance=post)
        post = Post.objects.all()

    return render(request, 'blog/post_edit.html', {
        'form': form,
        'post': post
    })
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    form = PostForm(instance=post)
    return render(request, 'blog/delete_result.html', {'form': form})

