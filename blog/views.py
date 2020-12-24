from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment
from like.models import LikeRecord
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.conf import settings
from taggit.models import Tag
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def user_home(request):
    '''
    context = {
        'posts': Post.objects.all()
    }
    '''
    return render(request, 'blog/base.html')


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(author=user)
    category = ''
    for post in Post.objects.filter(author=user):
        category += post.title + ', '
    category += 'etc.'

    context = {
        'user': user,
        'category': category,
    }
    return render(request, 'blog/user_profile.html', context)


def my_profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    category = ''
    for post in Post.objects.filter(author=user):
        category += post.title + ', '
    category += 'etc.'

    context = {
        'user': user,
        'category': category,
    }
    return render(request, 'blog/my_profile.html', context)

def user_follower(request):
    my_record = LikeRecord.objects.filter(user_id=request.user.pk) # 我给别人点赞的记录
    my_click = []
    for record in my_record:
        my_click.append(record.object_id) #我点过赞的id
    res = LikeRecord.objects.filter(user_id__in=my_click, object_id=request.user.pk)

    follower_id = []
    for record in res:
        follower_id.append(record.user_id)

    followers = User.objects.filter(id__in=follower_id)

    context = {
        'followers': followers
    }
    return render(request, 'blog/user_follower.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # naming convention <app>/<model>_<view type like detail>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(~Q(author=self.request.user))


class MyListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # naming convention <app>/<model>_<view type like detail>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

def my_list(request):
    object_list = Post.objects.filter(author=request.user)
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/home.html',{'page': page,'posts': posts})


def post_list(request, tag_slug=None):
    object_list = Post.objects.filter(~Q(author=request.user))
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/home.html',{'page': page,'posts': posts,'tag': tag})


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # naming convention <app>/<model>_<view type like detail>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                     'blog/post_detail.html',
                     {'post': post,
                      'user':user,
                      'comments': comments,
                      'new_comment': new_comment,
                      'comment_form': comment_form})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['title', 'content']
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    #fields = ['title', 'content']
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

