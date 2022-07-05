
import re
from urllib import request
from django.contrib import messages
from django.shortcuts import redirect, render
from .form import UserRegisterForm,PollForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Poll
# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Dear registration done successfully.")
            return redirect(poll_view)
        else:
            messages.error(request,'Registration unsuccessful.')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'login successfully.')
                return redirect(poll_view)
            else:
                messages.error(request,'Invalid credentials please try again.')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'logout successfully.')
    return redirect(home)
@login_required(login_url=home)
def profile(request):
    user_question = Poll.objects.filter(user=request.user)
    return render(request,'profile.html',{'poll':user_question})

@login_required(login_url=home)
def poll_view(request):
    poll = Poll.objects.all()
    return render(request,'poll_list.html',{'poll':poll})

def create_poll(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.user = request.user
            poll.save()
            messages.success(request,'poll added.')
            return redirect(poll_view)
        else:
            messages.error(request,'No poll Added.')
    else:
        form = PollForm()
    return render(request,'poll_create.html',{'form':form})

def vote(request,question_id):
    poll = Poll.objects.get(id=question_id)
    if request.method == 'POST':
        select_opt = request.POST['poll']
        if select_opt == 'option1':
            poll.counting_for_opt_one +=1
        elif select_opt == 'option2':
            poll.counting_for_opt_two +=1
        elif select_opt == 'option3':
            poll.counting_for_opt_three +=1
        elif select_opt == 'option4':
            poll.counting_for_opt_four +=1
        else:
            messages.error(request,'select atleast one option.')
            return redirect(result)
        poll.save()
        return redirect(result, question_id)
    return render(request,'poll_vote.html',{'poll':poll})
    
def result(reqeust,question_id):
    poll = Poll.objects.get(id=question_id)
    return render(reqeust,'result.html',{'poll':poll})
