from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import JobApplicationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'jobs/register.html', {'form': form})

def custom_logout_view(request):
    logout(request)
    return redirect('dashboard')  # Redirects to the dashboard directly after logging out

@login_required
def dashboard(request):
    status_filter = request.GET.get('status')
    if status_filter:
        jobs = JobApplication.objects.filter(user=request.user, status=status_filter)
    else:
        jobs = JobApplication.objects.filter(user=request.user)

    return render(request, 'jobs/dashboard.html', {'jobs': jobs})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def edit_job(request, job_id):
    job = JobApplication.objects.get(id=job_id, user=request.user)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})

@login_required
def delete_job(request, job_id):
    job = JobApplication.objects.get(id=job_id, user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('dashboard')
    return render(request, 'jobs/delete_job.html', {'job': job})


# Create your views here.
