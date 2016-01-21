from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list
    })


def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post_detail.html', {
        'post': post
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form
    })


def comment_new(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_id)
            comment.save()
            return redirect('blog:post_detail', post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {
        'form': form
    })


def comment_edit(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_id)
            comment.save()
            return redirect('blog:post_detail', post_id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/comment_form.html', {
        'form': form

    })


def comment_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', post_id)
    return render(request, 'blog/comment_delete.html', {
        'comment': comment
    })
