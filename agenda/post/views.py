from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm

class Home2(View):
	def get(self,request):
		return render(request,"inicio.html")


class Nuevo(View):
	def get(self,request):
		form=PostForm()
		context={
		'form':form,
		}
		return render(request,"nuevo.html",context)

	def post(self,request):
		form = PostForm(request.POST)
		form.save()
		return redirect('lista')



class Listado(View):
	def get(self,request):
		posts=Post.objects.all()
		form=PostForm()
		context={
		'posts':posts,
		#'form':form,
		}
		return render(request,"lista.html",context)

	def post(self,request):
		form = PostForm(request.POST)
		form.save()
		#context={
		#'posts':posts,
		#'form':form,
		#}
		#return render(request,"lista.html",context)
		return redirect('lista')