from django.shortcuts import render,redirect
from .models import UserProfile
from .forms import UserProfileForm
def edit_profile(request):

	try:
		profile = request.user.userprofile
	except UserProfile.DoesNotExist:
		profile = UserProfile(user=request.user)

	if request.method == 'POST':
		form = UserProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect(request,'edit_profile.html', {'form': form})
	else:
		form = UserProfileForm(instance=profile)
	return render(request,'edit_profile.html', {'form': form})