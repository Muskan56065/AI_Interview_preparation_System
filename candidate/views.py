

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CandidateProfile


@login_required
def create_profile(request):

    if request.method == 'POST':

        CandidateProfile.objects.update_or_create(
            user=request.user,
            defaults={
                'full_name': request.POST.get('full_name'),
                'phone': request.POST.get('phone'),
                'education': request.POST.get('education'),
                'experience': request.POST.get('experience'),
                'skills': request.POST.get('skills'),
                'target_role': request.POST.get('target_role'),
            }
        )

        return redirect('view_profile')

    return render(request, 'profile.html')


@login_required
def view_profile(request):

    profile = CandidateProfile.objects.filter(
        user=request.user
    ).first()

    return render(
        request,
        'view_profile.html',
        {'profile': profile}
    )