from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile


# ─── Landing Page ─────────────────────────────────────────────
def landing(request):
    return render(request, "landing/campuz-landing.html")


# ─── Signup ───────────────────────────────────────────────────
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm  = request.POST.get('confirm_password', '')

        # Validations
        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
            return render(request, 'landing/campuz-signup.html')

        if password != confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'landing/campuz-signup.html')

        if len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
            return render(request, 'landing/campuz-signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return render(request, 'landing/campuz-signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'landing/campuz-signup.html')

        # Create User
        user = User.objects.create_user(
            username = username,
            email    = email,
            password = password
        )

        # Create Profile
        Profile.objects.create(
            user              = user,
            role              = request.POST.get('role', '').strip(),
            contact           = request.POST.get('contact', '').strip(),
            enrollment_number = request.POST.get('enrollment_number', '').strip(),
            course            = request.POST.get('course', '').strip(),
            year              = request.POST.get('year', '').strip(),
            semester          = request.POST.get('semester', '').strip(),
            employee_id       = request.POST.get('employee_id', '').strip(),
            department        = (
                request.POST.get('department', '')
                or request.POST.get('admin_department', '')
            ).strip(),
            admin_code        = request.POST.get('admin_code', '').strip(),
        )

        messages.success(request, 'Account created! Please sign in.')
        return redirect('signin')

    return render(request, 'landing/campuz-signup.html')


# ─── Sign In ──────────────────────────────────────────────────
def signin(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier', '').strip()
        password   = request.POST.get('password', '')
        role       = request.POST.get('role', 'student')

        if not identifier or not password:
            messages.error(request, 'Both fields are required.')
            return render(request, 'landing/campuz-signin.html')

        # Find user based on role and identifier
        profile = None
        if role == 'student':
            profile = Profile.objects.filter(role='student', enrollment_number=identifier).first()
        elif role == 'faculty':
            profile = Profile.objects.filter(role='faculty', employee_id=identifier).first()
        elif role == 'admin':
            profile = Profile.objects.filter(role='admin', admin_code=identifier).first()

        # Determine username for authentication
        # Fallback to identifier if no profile is found (useful for superusers or existing accounts)
        auth_username = profile.user.username if profile else identifier

        user = authenticate(request, username=auth_username, password=password)

        if user is not None:
            login(request, user)
            
            # Redirect based on role if profile exists
            if profile:
                if profile.role == 'student':
                    return redirect('dashboard_student')
                elif profile.role == 'faculty':
                    return redirect('dashboard_faculty')
                elif profile.role == 'admin':
                    return redirect('dashboard_admin')
            
            return redirect('dashboard')
        else:
            role_labels = {
                'student': 'Enrollment Number',
                'faculty': 'Employee ID',
                'admin': 'Admin ID'
            }
            label = role_labels.get(role, 'Username')
            messages.error(request, f'Invalid {label} or password.')
            return render(request, 'landing/campuz-signin.html')

    return render(request, 'landing/campuz-signin.html')


# ─── Dashboards ───────────────────────────────────────────────
@login_required(login_url='signin')
def dashboard(request):
    """Generic dashboard entry point that redirects to role-specific dashboard."""
    try:
        profile = Profile.objects.get(user=request.user)
        if profile.role == 'student':
            return redirect('dashboard_student')
        elif profile.role == 'faculty':
            return redirect('dashboard_faculty')
        elif profile.role == 'admin':
            return redirect('dashboard_admin')
    except Profile.DoesNotExist:
        pass
    return render(request, 'landing/dashboard.html')


@login_required(login_url='signin')
def dashboard_student(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('signin')

    if profile.role != 'student':
        messages.error(request, "Access Denied: You do not have permission to view the Student Dashboard.")
        return redirect('dashboard')
    
    return render(request, 'landing/dashboard_student.html', {
        'profile': profile,
        'posts': []  # Placeholder for future feed functionality
    })


@login_required(login_url='signin')
def dashboard_faculty(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('signin')

    if profile.role != 'faculty':
        messages.error(request, "Access Denied: You do not have permission to view the Faculty Dashboard.")
        return redirect('dashboard')
    
    return render(request, 'landing/dashboard_faculty.html', {
        'profile': profile
    })


@login_required(login_url='signin')
def dashboard_admin(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('signin')

    if profile.role != 'admin':
        messages.error(request, "Access Denied: You do not have permission to view the Admin Dashboard.")
        return redirect('dashboard')
    
    return render(request, 'landing/dashboard_admin.html', {
        'profile': profile
    })


# ─── Placeholder Views for Student Dashboard ──────────────────
@login_required(login_url='signin')
def feed_create(request):
    messages.success(request, "Post created! (Placeholder)")
    return redirect('dashboard_student')

@login_required(login_url='signin')
def chatbot(request):
    from django.http import JsonResponse
    return JsonResponse({'reply': "Chatbot is coming soon! (Placeholder)"})

@login_required(login_url='signin')
def search(request):
    query = request.GET.get('q', '')
    return render(request, 'landing/dashboard_student.html', {
        'profile': Profile.objects.get(user=request.user),
        'query': query,
        'search_results': [],
        'posts': []
    })


# ─── Logout ───────────────────────────────────────────────────
def logout_view(request):
    logout(request)
    return redirect('signin')