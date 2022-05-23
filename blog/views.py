from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category, Tag,Team
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.utils import timezone

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category = None).count()
        return context

class PostCreate(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags'] 

    template_name = 'blog/post_update_forms.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category = None)

    else:
        category = Category.objects.get(slug = slug)
        post_list = Post.objects.filter(category = category)
        
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category = None).count(),
            'category': category, 
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug = slug)
    post_list = tag.post_set.all()
     
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag' : tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category = None).count(), 
        }
    )

def feedback_page(request):
    return render(
        request,
        'blog/feedback.html'
    )

def team_page(request):
    return render(
        request,
        'blog/teamMatching.html'
    )

def team_create(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.team_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', team_id=team.id)

# Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#      return render(
#          request,
#          'blog/index.html',
#          {
#              'posts':posts
#          }
#      )

#  def single_post_page(request, pk):
#      post = Post.objects.get(pk = pk)

#      return render(
#          request,
#          'blog/single_post_page.html',
#          {
#              'post':post
#          }
#     )