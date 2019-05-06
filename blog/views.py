from django.shortcuts import render
from django.utils import timezone
from .models import Post, Category
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import logging
from django.views.generic import TemplateView, ListView, DetailView

#@login_required
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
"""
#@login_required
def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
"""

#@login_required
def post_category_programming(request):
   posts=Post.objects.filter(category__contains="プログラミング").order_by('-published_date')
   return render(request, 'blog/post_list.html', {'posts': posts})

#@login_required
def post_category_cooking(request):
   posts=Post.objects.filter(category__contains="料理").order_by('-published_date')
   return render(request, 'blog/post_list.html', {'posts': posts})

#@login_required
class AboutMe_TemplateView(TemplateView):
   template_name="blog/about_me.html"

class PostDetailView(DetailView):

   model=Post
   template_name="blog/post_detail.html"

   """
   slug_field = "title"
   slug_url_kwarg = "title"
   """

   def get_queryset(self):
        categorytest=get_object_or_404(Category, category=self.kwargs['category'])
        return Post.objects.filter(category=categorytest).order_by('-published_date')

class PostListView(ListView):
   model=Post
   template_name="blog/post_list.html"

   def get_queryset(self):
       return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["category_data"] = str("このサイトには")+str(len(Post.objects.all()))+str("件の投稿があります")
        return context

class CategoryListView(ListView):

   model=Post
   template_name="blog/post_list.html"

   slug_url_kwarg="category"
   slug_field = "category"

   def get_queryset(self):
       categorytest=get_object_or_404(Category, category=self.kwargs['category'])
       return Post.objects.filter(category=categorytest).order_by('-published_date')

"""
   def get_context_data(self, **kwargs):
        category=get_object_or_404(Category, category=self.kwargs['slug'])
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        categories=Post.objects.filter(category=category).order_by('-published_date')
        #category_name=categories.category
        context["category_data"] = str(category.category)+str("カテゴリーの投稿は")+str(len(categories))+str("件あります")
        return context

"""

"""
class CategoryListView(ListView):
   model=Post
   template_name="blog/post_list.html"
   post=get_object_or_404(Post, pk=pk)
   post_category=post.category
   queryset=Post.objects.filter(category__contains=post_category).order_by('-published_date')

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["foo"] = len(queryset)
        return context

class PostDetailView(ListView):
    model = Post
    post_category=model.category
    queryset=Post.objects.filter(category__contains=post_category).order_by('-published_date')
    template_name="blog/post_list.html"

    def get_context_data(self, **kwargs):
        model=Post
        post_category=model.category
        post=Post.objects.filter(category__contains=post_category).order_by('-published_date')
        context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
        context["foo"] = len(post)
        return context

def get_category(request, pk):
   #categorys=Post.objects.all()
   category=get_object_or_404(Category, pk=pk)
   posts=Post.objects.filter(category_id=category).order_by('-published_date')
   return render(request, 'blog/post_list.html', {'posts': posts})


def get_latest_post(self):
        posts = Post.objects.filter(category=self)
        return render(request, 'blog/post_list.html', {'posts': posts})
def category_all(request):
    categorys=Category.objects.all()
    return render(request, 'blog/post_list.html', {'categorys': categorys})


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

