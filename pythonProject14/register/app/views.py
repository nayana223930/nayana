from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages

# Create your views here.
def reg(request):
    if request.method =="POST":

        u= request.POST['username']
        e=request.POST['email']
        p=request.POST['password']
        user=User.objects.create_user(username=u,email=e,password=p)
        user.save()
        messages.success(request,"successfully registered")
        return redirect("/")

    return render(request,"index.html")
def login(request):
    if request.method =="POST":
        username = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(email=username, password=password)
        if user is not None:
            auth.login(request, user)
        return redirect("re")
    return render(request, "index.html")
def re(request):

    return render(request, "re.html")