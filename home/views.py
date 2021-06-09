from django.shortcuts import render, redirect
from user.models import Usert
from board.models import Board


# Create your views here.


def home(request):
    user_id = request.session.get("user")
    all_boards = Board.objects.all().order_by("-id")

    if user_id:
        try:
            usert = Usert.objects.get(pk=user_id)
        except Usert.DoesNotExist:
            del request.session["user"]
            return redirect("/login")
        return render(request, "index.html", {"boards": all_boards, "username": usert.username})
    
    return render(request, "index.html", {"boards": all_boards})
    # 이전 if로 세션 처리를 했던 내용들을 template의 home.html로 이동시킴, html에서 session 처리가 가능함!
