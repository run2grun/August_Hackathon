from django.shortcuts import render


def signup(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 비밀번호 확인도 같다면
        if request.POST['password1'] ==request.POST['password2']:
            # 유저 만들기
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request,user) #로그인
            return redirect('home') # 블로그페이지
    # 포스트 방식 아니면 페이지 띄우기
    return render(request, 'signup.html')

def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서 
        username = request.POST['username']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(request, username=username, password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        # 실패
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 유저 로그아웃
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')