from django.shortcuts import render
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from blog.models import Post, Comment, Category
from .forms import CommentForm

def blog_index(request):
    lang = translation.get_language()
    posts = Post.objects.filter(
        language=lang, active=True
    ).order_by(
        '-created_on'
    )
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

def blog_category(request, category):
    lang = translation.get_language()
    posts = Post.objects.filter(
        categories__name__contains=category, language=lang, active=True
    ).order_by(
        '-created_on'
    )
    categoryObj = Category.objects.get(name=category)    
    context = {
        "category": categoryObj,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request, url):
    lang = translation.get_language()
    post = Post.objects.get(url=url, language=lang)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():            
            brothers = Post.objects.filter(
                code=post.code, active=True
            )            
            for brother in brothers:
                comment = Comment(
                    author=form.cleaned_data["author"],
                    email=form.cleaned_data["email"],
                    body=form.cleaned_data["body"],
                    post=brother
                )
                comment.gravatar = comment.gravatar_url()
                comment.save()

    comments = Comment.objects.filter(post=post)
    month_name = _(post.created_on.strftime("%B"))
    form = CommentForm()

    context = {
        "post": post,
        "date": post.created_on.strftime("%B %d, %Y") if lang == 'en' else ("{day} de {month} de {year}").format(day=post.created_on.day, month=month_name, year=post.created_on.year),
        "post_body": post.body,
        "comments": comments,
        "form": form,
    }
    
    return render(request, "blog_detail.html", context)
