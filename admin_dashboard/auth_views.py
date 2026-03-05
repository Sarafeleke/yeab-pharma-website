from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View

class AdminLoginView(View):
    def get(self, request):
        # Always redirect to login page, never show dashboard directly
        form = AuthenticationForm()
        return render(request, 'admin_dashboard/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', reverse_lazy('admin_dashboard:dashboard'))
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid credentials or insufficient permissions.')
        else:
            messages.error(request, 'Invalid username or password.')
        
        return render(request, 'admin_dashboard/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('admin_dashboard:login')
