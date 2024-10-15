# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # log the user in and them redirect to home page.
            login(request, new_user)
            return redirect("learning_logs:index")

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)
