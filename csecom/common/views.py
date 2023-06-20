from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserCreationForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            student_id = form.cleaned_data.get('student_id')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(student_id=student_id, password=raw_password)
            login(request, user)

            return redirect('main')
        
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

