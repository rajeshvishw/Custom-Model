from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm

def custom_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return render(request,'login.html',{'name':"user login"}) # Redirect to a success page
            else:
                return render(request,'login.html',{'name':'user not valid'})
        else:
            return redirect('/login/',{"name":"forms data not valid"})
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.hashers import make_password

def registration_view(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))  # Password ko hash hoga yaha pe
        user_bio = request.POST.get('user_bio')
        user_profile_image = request.FILES.get('user_profile_image')

        is_staff = request.POST.get('is_staff')
        if is_staff:
            isstaff = 1
        else:
            isstaff = 0
        is_superuser = request.POST.get('is_superuser')
        if is_superuser:
            issuperuser = 1
        else:
            issuperuser = 0
        # Create a new CustomUser object
        userss = CustomUser.objects.filter(phone_number = phone_number)
        if userss:
            warning = "Phone number must be unique"
            return render(request, 'registration.html',{"warning":warning})
        user = CustomUser(
            phone_number=phone_number,
            email=email,
            password=password,
            user_bio=user_bio,
            user_profile_image=user_profile_image,
            is_staff=isstaff,  # Set is_staff value
            is_superuser=issuperuser  # Set is_superuser value
        )
        user.save()

        # Koi aur additional action jaise ki welcome email bhejna aap kar sakte hain

        return redirect('/login/')  # Login page par redirect karein

    return render(request, 'registration.html')

