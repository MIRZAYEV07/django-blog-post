from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render , redirect
from .forms import PostForm,  LanguageForm
from .models import  PostLanguage , Language , Post ,TranslateLanguage
from deep_translator import GoogleTranslator
from .services import get_blogs_all,get_blog,get_my_blog

lan = 'en'



def make_blogs(request ):
    post = PostForm()
    code = LanguageForm()

    if request.POST:

        post = PostForm(request.POST, request.FILES)
        code = LanguageForm(request.POST)

        if post.is_valid() and code.is_valid():
            post.save()

            if post and code :

                qs1 = Language()
                qs1.code = code.cleaned_data['code']
                qs1.save()
                qs2 = PostLanguage()
                qs2.language_id = int(Language.objects.values('id').order_by('-id').first()['id'])
                qs2.post_id = int(Post.objects.values('id').order_by('-id').first()['id'])
                qs2.save()
                return redirect('blogs')


    ctx = {
        'post': post,
        'code': code,


    }

    return render(request, "blogs/make_blogs.html", ctx)

def my_blogs(request ,user_u):
    forms = get_my_blog(user_u)
    ctx = {
        "forms":forms
    }

    return render(request, "blogs/my_blogs.html", ctx)

def blogs_detail(request,slug):
    forms = get_blog(slug)
    ctx = {
        "forms": forms
    }

    return render(request, "blogs/blog.html", ctx)





def blogs(request):
    per_page = 5
    forms = get_blogs_all()

    p = Paginator(forms, per_page)

    p_num = request.GET.get('page', 1)
    print(">>>>>>>>", p_num)
    m = p_num
    p_num = int(p_num)

    p_object = p.get_page(p_num)
    p_count = p.num_pages
    pages = []

    a = 0
    for i in range(p_num, p_count + 1):
        a += 1
        pages.append(i)
        if a == 3:
            break
    a = len(pages)
    if len(pages) != 3:
        while a != 3:
            a = len(pages)
            i = pages[0] - 1
            pages.append(i)
            pages.sort()

            a += 1

    ctx = {
        'forms': p_object,
        'p_count': pages,
        "p_num": p_num,
        'a': m,
        'q': p_count

    }

    return render(request, 'blogs/blogs.html', ctx)
