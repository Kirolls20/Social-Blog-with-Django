from django.shortcuts import render,redirect, get_object_or_404
from django.views import generic
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreatePostForm, CommentForm
from .models import Post,Comment, User

#------------------------------------------Classes----------------------------------------#

class LandingView(generic.TemplateView):
   template_name='landing.html'

# Create Post Form View 
class CreatePostView(LoginRequiredMixin,generic.CreateView):
   template_name='create_post.html'
   model=Post
   form_class = CreatePostForm
   
   def get_success_url(self):
      return reverse_lazy('post-list')

   def form_valid(self,form):
      obj= form.save(commit=False)
      obj.owner= self.request.user
      obj.save()
      super(CreatePostView,self).form_valid(form)

# List all posts View

class ListPostView(generic.ListView):
   template_name='post_list.html'
   context_object_name='post_list'
   model=Post

   # def get_context_data(self,**kwargs):
   #    context = super(ListPostView, self).get_context_data(**kwargs)
   #    context['total_likes'] = Post.objects.values('likes').count()
   #    return context


# Post Deatail View 
class DetailPostView(LoginRequiredMixin,generic.DetailView):
   template_name='post_detail.html'
   model=Post
   
   def get(self,request,pk):
      post= Post.objects.get(id=pk)
      data=get_object_or_404(Post,id=pk)
      total_likes= data.total_likes()
      total_comments = data.total_comments()
      lastest_posts = Post.objects.order_by('-updated_at')[:3]
      comment_form = CommentForm
    
      comments = Comment.objects.filter(post=post).order_by("-updated_at")
      ctx = {'post': post, 'total_likes': total_likes, 
         'comment_form': comment_form, 
             'comments': comments, 'lastest_posts': lastest_posts, 'total_comments': total_comments}
      return render(request, self.template_name, ctx)
   
# Delete Post View
class DeletePostView(LoginRequiredMixin,generic.DeleteView):
   template_name='post_delete.html'
   model=Post
   def get_success_url(self):
      return reverse_lazy('post-list')

# Update Post View
class UpdatePostView(LoginRequiredMixin,generic.UpdateView):
   template_name= 'post_update.html'
   model=Post
   form_class = CreatePostForm
   success_url=reverse_lazy('post-list')
   
   def get_queryset(self):
      qs = super(UpdatePostView,self).get_queryset()
      return qs.filter(owner=self.request.user)

# Comment View
class CreateCommentView(LoginRequiredMixin,View):
   def post(self,request,pk):
      post_id= get_object_or_404(Post,id=pk)
      comment=Comment(comment_body=request.POST['comment_body'],owner=self.request.user,post=post_id)
      comment.save()
      return redirect(reverse('post-details',args=[pk]))

#-------------------------------Functions-----------------------------------------------------#
# function to Add like to post
def add_like(request, pk):
   post = get_object_or_404(Post, id=request.POST.get('post_id'))
   post.likes.add(request.user)
   return redirect(reverse('post-details', args=[pk]))

# Search for caegory Function
def search_category_view(request):
   template_name = 'search_category.html'
   if request.method == 'POST':
      search_category = request.POST['search-category']
      searched_posts = Post.objects.filter(catogery__contains=search_category)
      ctx = {'search_category': search_category,'searched_posts': searched_posts}
      return render(request,template_name,ctx)
   else:
      return render(request, template_name, {})



