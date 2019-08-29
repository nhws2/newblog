from django.shortcuts import render,redirect
from .models import bulletin,Comment
from django.core.paginator import Paginator

def index(request):
    posts = bulletin.objects.all()
    paginator = Paginator(posts,4)
    now_page = request.GET.get('page')
    posts = paginator.get_page(now_page)
    context={
        "posts":posts,
    }
    return render(request,'index.html',context)

def create(request):
    if request.method == "GET":
        return render(request,'create.html')

    elif request.method == "POST":
        post = bulletin()
        post.user = request.user
        post.subject = request.POST['subject']
        post.content = request.POST['content']
        post.save()

        return redirect(index)

def read(request,post_id):
    post = bulletin.objects.get(id = post_id)
    comment = Comment.objects.filter(post=post.id)
    context = {
        "post":post,
        "comment":comment,
    }
    return render(request,'read.html',context)

def update(request,post_id):
    if request.method == "GET":
        post = bulletin.objects.get(id = post_id)
        context = {
            "post":post,
        }
        return render(request,'update.html',context)

    elif request.method == "POST":
        post = bulletin.objects.get(id = post_id)
        post.subject = request.POST['subject']
        post.content = request.POST['content']
        post.save()

        return redirect(index)

def delete(request,post_id):
    post = bulletin.objects.get(id = post_id)
    post.delete()

    return redirect(index)

def c_create(request,post_id):
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.post = bulletin.objects.get(id=post_id)
        comment.content = request.POST['comment']
        anonymous = request.POST.get('anonymous',False)
        if anonymous == "y":
            comment.anonymous = True
        comment.save()
        return redirect(read,comment.post.id)
