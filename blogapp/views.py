from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .models import BlogPost,Profile
from django.contrib.auth.models import User,auth
from .forms import ProfileUpdateForm,UserUpdateForm,BlogUpdateForm
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login

@login_required
def bloghome(request):
    profile=Profile.objects.all()
    blogs = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(blogs,6) 
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'blogs': blogs,'page_obj':page_obj,'profl':profile})

@login_required
def userblog(request):
    user = request.user.id 
    userblogs = BlogPost.objects.filter(author=user).order_by('-created_at')
    paginator = Paginator(userblogs,6) 
    page_number = request.GET.get('page')  
    page_obj1 = paginator.get_page(page_number)
    print(userblogs)
    return render(request,'userblogs.html',{'usblgs': userblogs ,'us':user,'page_obj1':page_obj1})

@login_required   
def create_blog_post(request):
    form = BlogUpdateForm()

    if request.method == 'POST':
        form = BlogUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            pca = form.save(commit=False)
            pca.author = request.user  
            pca.save()
            return redirect('/home')  
        form = BlogUpdateForm()  

    return render(request, 'createblogpost.html', {'bf': form})

@login_required   
def updateblogpost(request, pk):
    a = get_object_or_404(BlogPost, id=pk)

    if request.method == "POST":    
        if a.author == request.user: 
            c = BlogUpdateForm(request.POST, instance=a)  
            if c.is_valid():
                c.save()
                return redirect('/userblogs')
            else:
                return HttpResponse("<h1>Sorry, form validation failed.</h1>")
        else:
            return HttpResponse("<h1>You are not authorized to edit this post.</h1>")
    else:
        c = BlogUpdateForm(instance=a)
        return render(request, 'editblogpost.html', {'cf': c})
@login_required
def snglblogview(request, pk):
    blog_post = get_object_or_404(BlogPost, id=pk) 
    return render(request, 'singleblog.html', {'sblog': blog_post}) 
    

@login_required
def deleteblogpost(request, pkd):
    blog_post = get_object_or_404(BlogPost, id=pkd)
    
    if request.method == "POST":
        if blog_post.author == request.user:
            blog_post.delete()
            return redirect('/userblogs') 
        else:
            return HttpResponse("<h1>You are not authorized to delete this post.</h1>")
    
    return HttpResponse("<h1>Invalid request method.</h1>")



def signupfn(request):
    if request.method == 'POST':
        un = request.POST['uname']
        na = request.POST['fname']
        em = request.POST['email']
        pa1 = request.POST['pass1']
        pa2 = request.POST['pass2']

        if pa1 == pa2:
            if User.objects.filter(username=un).exists():
                messages.error(request, "Username taken")
            elif User.objects.filter(email=em).exists():
                messages.error(request, "Email already in use")
            else:
                User.objects.create_user(username=un, email=em, first_name=na, password=pa1)
                messages.success(request, "Account created succesfully")
                return redirect('/')  
        else:
            messages.error(request, "Passwords do not match")
    return render(request, 'signup.html')


def loginfn(request):
     if request.method == 'POST':
            u=request.POST['a']
            pa=request.POST['b']

            c=auth.authenticate(username=u,password=pa)

            if c:
                auth.login(request,c)
                return redirect('/home')
            
            else:
                messages.error(request,"Sorry, your password was incorrect. Please double-check your password")
                return redirect('/')
    
     else:
        return render(request,'login.html')
     
def logoutfn(request):
        auth.logout(request)
        return redirect('/')

@login_required
def profile_view(request):
    user = request.user 
    blog_count = BlogPost.objects.filter(author=user).count()  
    profile_picture = user.profile.profile_picture.url if user.profile.profile_picture else '/static/images/default.jpg'
    return render(request, 'profileview.html', {'us':user,'pp':profile_picture,'blog_count': blog_count})

        
@login_required  
def profileedit(request):
    user = request.user 

    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        return HttpResponse("<h1>Profile not found</h1>")  

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            if User.objects.exclude(pk=user.pk).filter(username=user_form.cleaned_data.get('username')).exists():
                user_form.add_error('username', 'This username is already taken.')
            
            if User.objects.exclude(pk=user.pk).filter(email=user_form.cleaned_data.get('email')).exists():
                user_form.add_error('email', 'This email is already in use.')
            
            if not user_form.errors: 
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('/profileview')  

    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, 'profileform.html', {
        'usf': user_form,
        'prf': profile_form,
    })

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['POST'])
def create_blog_post_api(request):
    serializer = BlogPostSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET'])
def get_blog_post(request, pk):
    try:
        blog = BlogPost.objects.get(pk=pk)
        serializer = BlogPostSerializer(blog)
        return Response(serializer.data)
    except BlogPost.DoesNotExist:
        return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_all_blog_posts(request):
    blogs = BlogPost.objects.all()  
    serializer = BlogPostSerializer(blogs, many=True)  
    return Response(serializer.data, status=status.HTTP_200_OK)     

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['PUT'])
def update_blog_post(request, pk):
    try:
        blog = BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogPostSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['DELETE'])
def delete_blog_post(request, pk):
    try:
        blog = BlogPost.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except BlogPost.DoesNotExist:
        return Response({'error': 'Blog post not found'}, status=status.HTTP_404_NOT_FOUND)
