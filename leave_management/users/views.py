from django.shortcuts import render, redirect
from .models import User
from .forms import SignupForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            token = user.generate_verification_token()
            user.save()
            verification_link = f"http://127.0.0.1:8000/verify-email/{token}/"
            send_mail(
                'Verify your email',
                f'Click here to verify your email: {verification_link}',
                'from@example.com',
                [user.email],
            )
            messages.success(request, "Signup successful! Check your email to verify account.")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

# Verify Email
def verify_email(request, token):
    user = User.objects.filter(verification_token=token).first()
    if user:
        user.email_verified = True
        user.verification_token = ''
        user.save()
        return render(request, 'users/email_verified.html', {'message': 'Email verified successfully!'})
    return render(request, 'users/email_verified.html', {'error': 'Invalid or expired token!'})

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email).first()
        if user and user.email_verified and user.check_password(password):
            request.session['user_id'] = user.id
            request.session['role'] = user.role
            return redirect('dashboard')
        messages.error(request, "Invalid credentials or email not verified")
    return render(request, 'users/login.html')

# Logout
def logout_view(request):
    request.session.flush()
    return redirect('login')

# Dashboard
def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = User.objects.get(id=user_id)
    return render(request, 'users/dashboard.html', {'user': user})

# No Access Page
def no_access(request):
    return render(request, 'users/no_access.html')


def home(request):
    return render(request, 'users/home.html')
