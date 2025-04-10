from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup
from django.contrib.auth import authenticate, login
# Create your views here.




def signup(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Simple validation to check if fields are filled
        if username and first_name and last_name and email and password:
            try:
                # Create a new Signup instance and save it to the database
                new_user = Signup(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                new_user.save()
                # Success message
                messages.success(request, 'Account created successfully!')
                return redirect('login:login')  # Redirect to the login page after successful signup

            except Exception as e:
                # If there is an error, show an error message
                messages.error(request, 'Account could not be created. Please try again.')
                return redirect('signup')  # Stay on the signup page if there is an error
        else:
            # If any required fields are empty, show an error message
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'signup.html')






def home(request):
    return render(request, 'home.html')






def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            # Try to get the user by username
            user = Signup.objects.get(username=username)

            # Check if the password matches exactly (case-sensitive)
            if user.password == password:
                messages.success(request, 'Login successful!')
                
                
                # Set session data
                request.session['is_logged_in'] = True  # Store session variable
                request.session['username'] = user.username
                
                
                return redirect('diseases:capture')  # Redirect to your home page after successful login
            else:
                messages.error(request, 'Invalid password! Passwords must match exactly.')
                return render(request, 'login.html')

        except Signup.DoesNotExist:
            # If user is not found, show an error message
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')

    # For GET requests, render the login page
    return render(request, 'login.html')




