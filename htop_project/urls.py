from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Add this function to redirect root URL to /htop
def redirect_to_htop(request):
    return redirect('/htop')

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add root URL pattern to redirect to /htop
    path('', redirect_to_htop, name='root'),
    path('htop/', include('htop_app.urls')),  # Note the trailing slash
]