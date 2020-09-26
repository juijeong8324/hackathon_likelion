from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Account, Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        logineduser = Account.objects.get(user = request.user)
        context = {'user':logineduser}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        userid = request.POST['id']
        userpw = request.POST['password']
        user = auth.authenticate(request, username=userid, password=userpw)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, "회원 정보가 일치하지 않습니다.")
            return redirect('login')
    
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        userid = request.POST.get('id')
        userpw1 = request.POST.get('password1')
        userpw2 = request.POST.get('password2')
        username = request.POST.get('name')
        useremail = request.POST.get('email')

        if userid == "" or userpw1 == "" or userpw2 == "" or username == "" or useremail == "":
            messages.info(request, "모든 항목을 입력해주세요.")
            return redirect('signup')

        if userpw1 != userpw2:
            messages.info(request, "비밀번호를 확인해주세요.")
            return redirect('signup')
        
        user = User.objects.create_user(username=userid, password=userpw1)
        user.save()
        account = Account(user=user, name=username, email=useremail)
        account.save()
        return redirect('login')
    
    else:
        return render(request, 'signup.html')
    




    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def notice(request):
    posts = Post.objects.all().order_by('id')
    context = {'posts':posts}
    return render(request, 'notice.html', context)

def detail(request, post_id):
    posts = Post.objects.all().order_by('id')
    post_detail = get_object_or_404(Post, pk = post_id)
    post_detail.views = post_detail.views + 1
    post_detail.save()
    prevpostid = post_detail.id - 1
    nextpostid = post_detail.id + 1
    context = {'posts':posts, 'post':post_detail, 'prevpostid':prevpostid, 'nextpostid':nextpostid}
    return render(request, 'detail.html', context)

def page2(request):
    return render(request, 'page2.html')