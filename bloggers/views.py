from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from bloggers.forms import SignUpForm, Post_Form
from bloggers.models import Blog
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def landing(request):
	if request.user.is_authenticated:
		return render(request,'bloggers/landing.html')	
	else:	
		return render(request,"bloggers/landing.html")

@login_required
def post_blog(request):
    post_form = Post_Form()
    dict_data = {'postform':post_form}
    if request.method=='POST':
        post_form = Post_Form(request.POST,request.FILES)
        if post_form.is_valid():
            post_data = post_form.save()
            post_data.author = request.user.first_name+' '+request.user.last_name
            post_data.save()
            dict_data.update({'msg':'Posted Successfully'})
    return render(request,'bloggers/postblog.html',dict_data)

def view_blog(request):
    blog_post = Blog.objects.all().order_by('-upload_datetime')
    dict_data = {'data':blog_post}
    if request.method=='POST':
        data = request.POST['id']
        blog_post = Blog.objects.filter(id=data)
        blog_post.delete()
        dict_data.update({'data':blog_post,'msg':'Post Deleted Successfully'})
    return render(request,'bloggers/viewblog.html',dict_data)

def read_blog(request):
    data = request.GET['id']
    blog_post = Blog.objects.filter(id=data)
    return render(request,'bloggers/readblog.html',{'data':blog_post})

def signuppage(request):
    signupform=SignUpForm()
    dict_data = {'signupform':signupform}
    if request.method=='POST':
        signupform=SignUpForm(request.POST)
        if signupform.is_valid():                    # Required for email sending
            user=signupform.save()
            user.set_password(user.password)
            user.save()
            # Email Sending on Signup
            subject = "Welcome To Blog Site Testing"
            message = "Welcome "+user.first_name+", you are Registered"
            recipient_list = [user.email]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)

            dict_data.update({'msg':'Registered Successfully'})
    return render(request,'bloggers/signup.html',dict_data)

# def delete_post(request,id):
#     blog_post = Blog.objects.filter(id=id)
#     return HttpResponseRedirect('/viewblog/')