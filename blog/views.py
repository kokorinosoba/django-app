from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template.context_processors import csrf
from .models import Post
from .forms import PostForm, ChkForm, Credits


# Create your views here.
def calc_credit(request):
    credits = Credits()
    return render(request, 'calc_credit.html', {'credits': credits})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def demo3(request):
    labels = ['チェック', '複数チェック', 'ラジオボタン', '動的選択肢１', '動的選択肢２']
    # 入力結果を格納する辞書
    results = {}
    radios = {}
    ret = ''
    if request.method == 'POST':
        # 入力されたデータの受取
        results[labels[0]] = request.POST.getlist("one")
        results[labels[1]] = request.POST.getlist("two")
        results[labels[2]] = request.POST.getlist("three")
        results[labels[3]] = request.POST.getlist("four")
        results[labels[4]] = request.POST.getlist("five")
        ret = 'OK'
        c = {'results': results, 'ret': ret}
    else:
        form = ChkForm()
        choice1 = []
        choice1.append(('1', '動的選択肢１'))
        choice1.append(('2', '動的選択肢２'))
        choice1.append(('3', '動的選択肢３'))
        choice1.append(('4', '動的選択肢４'))
        form.fields['four'].choices = choice1
        form.fields['four'].initial = ['2']
        form.fields['five'].choices = choice1
        form.fields['five'].initial = ['3']
        c = {'form': form, 'ret': ret}
        # CFRF対策（必須）
        c.update(csrf(request))
    return render(request, 'demo03.html', c)
