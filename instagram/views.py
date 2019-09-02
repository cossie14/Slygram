
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewStoryForm, NewCommentForm
from .models import Image, Profile, Comments

# Create your views here.
@login_required(login_url='/accounts/login/')
def newsfeed(request):
    current_user = request.user
    images = Image.objects.all()
    profiles = Profile.objects.all()
    comments = Comments.objects.all()
    return render(request, 'newsfeed.html', {'images':images, 'profiles':profiles, 'profile':profile, 'comments':comments})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.id)
    images = Image.objects.all().filter(profile_id=current_user.id)
    return render(request, 'profile.html', {'images':images, 'profile':profile})

@login_required(login_url='/accounts/login/')
def new_story(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'Post':
        form = NewStatusForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            image.user = request.user
            image.save()
        return redirect('')
    else:
        form = NewStoryForm()
    return render(request, 'new_story.html', {"form": form})

@login_required(login_url='/accounts/login')
def user_profile(request, user_id):
    profile = Profile.objects.get(id=user_id)
    images = Image.objects.all().filter(user_id=user_id)
    return render(request, 'profile.html', {'profile':profile, 'images':images})

@login_required(login_url='/accounts/login')
def single_pic(request, photo_id):
    image = Image.objects.get(id = photo_id)
    return render(request, 'single_pic.html', {'image':image})

def profile(request):
    if 'images' in request.GET and request.GET['images']:
        search_term = request.GET.get('images')
        searched_image = Image.search_by_user(search_term)
        return render(request, 'profile.html', {'images':searched_image})
    else:
        message = 'You haven\'t searched for anything'
        return render(request, 'single_pic.html')

@login_required (login_url='/accounts/register/')
def single_pic_like(request, photo_id):
    image = Image.objects.get(id=photo_id)
    image.likes = image.likes + 1
    image.save()
    return redirect('')

@login_required(login_url='/accounts/login/')
def new_comment(request, username):
    current_user = request.user
    username = current_user.username
    if request.method == 'POST':
        form = NewCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            comment.user = request.user
            comment.save()
        return redirect('')
    else:
        form = NewCommentForm()
    return render(request, 'comment.html', {"form": form})
