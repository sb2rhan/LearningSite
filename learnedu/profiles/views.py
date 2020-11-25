from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Profile, Post, Course
from .forms import PostForm, ProfileForm, CourseForm


@login_required(login_url='/auth/login')
def profile_page(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    context = {
        'profile': profile,
        'post_form': PostForm(),
        'profile_form': ProfileForm(instance=profile),
    }

    return render(request, 'profile/profile_detail.html', context)


@login_required(login_url='/auth/login')
def courses_page(request, username):
    profile = Profile.objects.get(user=User.objects.get(username=username))

    context = {
        'profile': profile,
        'courses': Course.objects.all().filter(is_active=True),
        'enrolled_courses': profile.courses.filter(is_active=True),
        'form': CourseForm()
    }
    return render(request, 'profile/courses_page.html', context)


@login_required(login_url='/auth/login')
def course_detail(request, username, id):
    course = Course.objects.get(pk=id)
    profile = request.user.profile

    context = {
        'course': course,
        'is_enrolled': True if profile.courses.filter(pk=id) else False
    }

    return render(request, 'profile/course_detail.html', context)


@login_required(login_url='/auth/login')
def course_enroll(request, username, id):
    course = Course.objects.get(pk=id)
    profile = request.user.profile

    if not profile.courses.filter(pk=id):
        profile.courses.add(course)
        course.enroll_count += 1
        course.save()

    return redirect(reverse('courses_page', kwargs={ 'username': username }))


@login_required(login_url='/auth/login')
def course_unenroll(request, username, id):
    course = Course.objects.get(pk=id)
    profile = request.user.profile

    if profile.courses.filter(pk=id):
        profile.courses.remove(course)
        course.enroll_count -= 1
        course.save()

    return redirect(reverse('courses_page', kwargs={ 'username': username }))


@login_required(login_url='/auth/login')
def course_delete(request, username, id):
    course = Course.objects.get(pk=id)

    course.is_active = False
    course.save()

    return redirect(reverse('courses_page', kwargs={ 'username': username }))


@login_required(login_url='/auth/login')
def create_post(request, username):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.profile = request.user.profile
            post.save()
            form.save_m2m()
        else:
            print('Create post form is not valid')

    return redirect(reverse('profile_page', kwargs={ 'username': username }))


@login_required(login_url='/auth/login')
def create_course(request, username):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user.profile
            course.save()
            form.save_m2m()
        else:
            print('Create course form is not valid')

    return redirect(reverse('courses_page', kwargs={ 'username': username }))


@login_required(login_url='/auth/login')
def delete_post(request, username, id):
    post = Post.objects.get(pk=id)
    post.is_active = False
    post.save()
    return redirect(reverse('profile_page', kwargs={ 'username': username }))


@login_required(login_url='/auth/login')
def edit_profile(request, username):
    p = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=p)

        if form.is_valid():
            profile_ = form.save(commit=False)
            profile_.user = request.user
            profile_.save()
            form.save_m2m()
        else:
            print('Edit profile form is not valid')

    return redirect(reverse('profile_page', kwargs={ 'username': username }))
