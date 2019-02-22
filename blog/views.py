from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.views import generic
from .models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.models import User

from .form import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def index(request):
    return render(request, 'blog/index.html')


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 4
    # template_name = 'blogs/blog_list.html'

class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Blog
    context_object_name = 'blog_post'
    # template_name = 'blog/blog_post.html'


class BloggerListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5


class BlogsByAuthorListView(generic.ListView):
    """
    View for a list of blogs posted by a particular blogger
    """
    model = Blog
    paginate_by = 5
   # template_name = 

    def get_queryset(self):
        """
        Return list of Blog objects created by BlogAuthor
        """
        id = self.kwargs['pk']
        by_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=by_author)

    def get_context_data(self, **kwargs):
        """
        Add BlogAuthor to context so they can be displayed in the template
        """
        context = super(BlogsByAuthorListView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context


@login_required(login_url='login')
def add_comment_to_blog(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.author = auth.get_user(request)
            comment.save()
            return redirect('blog-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_blog.html', {'form': form})



def delete_comment(request, comment_id):
    comment = get_object_or_404(BlogComment, pk=comment_id)
    blog_id = comment.blog.id
    if comment.author == request.user:
        comment.delete()
    return redirect('blog-detail', blog_id)
