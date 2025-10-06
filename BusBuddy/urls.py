"""
URL configuration for BusBuddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# project_name/urls.py (Main Project File)

# project_name/urls.py (Corrected)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # CRITICAL FIX: Include Django's built-in authentication URLs
    # This provides the global names: 'login', 'logout', 'password_reset', etc.
    path('accounts/', include('django.contrib.auth.urls')), 
    
    # Wire up the core application URLs under the root path
    path('', include('core.urls', namespace='core')), 
]