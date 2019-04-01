from django.shortcuts import render,redirect
from .forms import signup1,login1
from .models import profile
from django.contrib.auth import get_user_model,login
# Create your views here.




User=get_user_model()
def register(request):
	form_class=signup1(request.POST or None)
	context={
		'bool':False,
	}
	print(form_class.is_valid())
	if request.POST:
		username=request.POST.get('username')
		objs=User.objects.filter(username=username)
		if objs.count()>0:
			context={
				'bool':True
			}
		else:
			name=request.POST.get('name')
			password=request.POST.get('password')
			sid=request.POST.get('sid')
			token=request.POST.get('token')
			mobile=request.POST.get('mobile')
			user_new=User.objects.create_user(username=username,email=username,password=password)
			user_new1=profile.objects.create(
				username=username,
				name=name,
				sid=sid,
				token=token,
				mobile=mobile
				)
			return redirect("/congo")
	return render(request,"register.html",context)


def login2(request):
	form_class=login1(request.POST or None)
	context={
		"form": form_class
	}
	print("User Logged in")
	if form_class.is_valid():
		email=form_class.cleaned_data.get("username")
		password=form_class.cleaned_data.get("password")
		user = User.objects.filter(username=email)
		if user is not None:
			user=user.first()
			login(request,user)
			return redirect("/")
		else:
		    print("Error")
	return render(request,"login.html",context)