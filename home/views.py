from django.shortcuts import render
from user.models import Usert
from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    user_id = request.session.get("user")

    if user_id:
        try:
            usert = Usert.objects.get(pk=user_id)
        except Usert.DoesNotExist:
            del request.session["user"]
            return redirect("/")
        
        return render(request, "index.html",usert)

    return render(request, "index.html")
    # return render(request, "blog/index.html")
    # 이전 if로 세션 처리를 했던 내용들을 template의 home.html로 이동시킴, html에서 session 처리가 가능함!


def login(request):
    return render(request, "login.html")