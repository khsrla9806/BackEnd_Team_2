from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from .forms import PostForm, ScheduleForm
from .models import Post, Schedule
from django.urls import reverse

def home(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    return render(request, 'index.html', context)

def team_intro(request):
    return render(request, 'backend_team.html')

def post_list(request):
    post_objects = Post.objects.order_by('-created_at')
    context = {'post_objects' : post_objects}
    return render(request, 'post_list.html', context)

def post_detail(request, pk):
    post_detail_object = Post.objects.get(pk=pk)
    context = {'post_detail_object' : post_detail_object}
    return render(request, 'post_detail.html', context)

# class PostCreate(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'post_create.html'
#     success_url = '/post_list/'

def post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        if schedule_form.is_valid():
            schedule = schedule_form.save(commit=False)
            if post_form.is_valid():
                post = post_form.save() # post_form이 DB에 저장됨.
                # post_form DB에 저장된 내용 중 post_id에 해당하는 값을 schedule_form의 post_id에 저장해야 한다.
                schedule.post_id = post.pk
                schedule_form.save()
                return redirect('post_list')
        else:
            return render(request, 'post_create.html', context)
    else:
        post_form = PostForm(request.POST)
        schedule_form = ScheduleForm(request.POST)
        context = {'post_form':post_form, 'schedule_form':schedule_form}
        return render(request, 'post_create.html', context)
        
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.author = request.POST['author']
        post.created_at = post.updated_at
        
        post.save()
        return redirect('post_detail', post.pk)
    else:
        postForm = PostForm(instance = post) # instance = post 를 사용하면 post에 저장되어 있던 이전 내용들을 모두 불러옵니다. 
        return render(request, 'post_edit.html', {'postForm':postForm})
    
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
        
def company_list(request):
    return render(request, 'company_list.html')

def company_detail(request):
    return render(request, 'company_detail.html')