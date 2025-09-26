from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Leave
from .forms import LeaveForm
from users.models import User

# Decorators
def employee_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('role') == 'Employee':
            return view_func(request, *args, **kwargs)
        return redirect('no_access')
    return wrapper

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('role') == 'Admin':
            return view_func(request, *args, **kwargs)
        return redirect('no_access')
    return wrapper

# Apply Leave
@employee_required
def apply_leave(request):
    user = User.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = user
            leave.save()
            return redirect('leave_history')
    else:
        form = LeaveForm()
    return render(request, 'leaves/apply_leave.html', {'form': form})

# Leave History
@employee_required
def leave_history(request):
    user = User.objects.get(id=request.session['user_id'])
    leaves = Leave.objects.filter(user=user)
    return render(request, 'leaves/leave_history.html', {'leaves': leaves})

# Admin Dashboard (Pending Leaves)
@admin_required
def admin_dashboard(request):
    leaves = Leave.objects.filter(status='Pending')
    return render(request, 'leaves/admin_dashboard.html', {'leaves': leaves})

# Approve / Reject Leave
@admin_required
def update_leave_status(request, leave_id, action):
    leave = Leave.objects.get(id=leave_id)
    if action in ['Approved', 'Rejected']:
        leave.status = action
        leave.save()
    return redirect('admin_dashboard')
