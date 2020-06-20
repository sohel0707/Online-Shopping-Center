from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import Shoes,SingleShoes,Orders,OrderUpdate
import json
# Create your views here.
def index(request):
	shoes=Shoes.objects.all()
	return render(request,'index.html',{'shoes':shoes})


def logout(request):
	auth.logout(request)
	return redirect('/')


def login(request):
	if request.method == 'POST':
		password=request.POST['password']
		username=request.POST['username']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.error(request,"Invalid credentials")
			return redirect('login')
	else:
		return render(request,'login.html')


def register(request):
	if request.method == 'POST':
		firstname=request.POST['first_name']
		lastname=request.POST['last_name']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		username=request.POST['username']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username taken")
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email taken")
				return redirect('register')
			else:
				user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,password=password1,username=username)
				user.save()
				return redirect('/login')
		else:
			messages.info(request,"Password not match")
			return redirect('register')
	else:
		return render(request,'register.html')


def single(request,id):
	shoe=Shoes.objects.get(id=id)
	singleshoes=SingleShoes.objects.all()
	for singleshoe in singleshoes:
		if shoe.name==singleshoe.name:		
			return render(request,'single-product.html',{'singleshoe':singleshoe})


	


def confirmation(request):
	return render(request,'confirmation.html')



def checkout(request):
	if request.method == 'POST':
		item_json=request.POST['itemjson']
		username=request.POST['username']
		password=request.POST['password']
		address1=request.POST['address1']
		address2=request.POST['address2']
		city=request.POST['city']
		zipcode=request.POST['zipcode']
		state=request.POST['state']
		phone=request.POST['phone']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			order=Orders(item_json=item_json,username=username,password=password,address1=address1,address2=address2,city=city,zipcode=zipcode,phone=phone,state=state)
			order.save()
			update=OrderUpdate(order_id=order.id,update_desc="The Order has been placed")
			update.save()
			thank=True
			id=order.id
			return render(request,'checkout.html',{'thank':thank,'id':id})
		else:
			messages.error(request,"Invalid credentials")
	return render(request,'checkout.html')


def category(request):
	return render(request,'category.html')


def cart(request):
	return render(request,'cart.html')


def contactus(request):
	return render(request,'contact.html')


def aboutus(request):
	return render(request,'about.html')

def tracker(request):
	if request.method == 'POST':
		order_id=request.POST['orderid']
		username=request.POST['username']
		password=request.POST['password']
		#return HttpResponse(f"{order_id} and {username} and {password}")
		try:
			order=Orders.objects.filter(id=order_id,username=username,password=password)
			if len(order)>0:
				update=OrderUpdate.objects.filter(order_id=order_id)
				updates=[]
				for item in update:
					updates.append({'text':item.update_desc,'time':item.timestamp})
					response=json.dumps(updates,default=str)
				return HttpResponse(response)
			else:
				return HttpResponse('{}')
		except Exception as e:
			return HttpResponse('{}')
	return render(request,'tracker.html')