from django.contrib import admin
from django.urls import path, include  # Add this import to include the 'path' function
from django.views.generic import RedirectView
from django.conf import settings  # Import settings for serving media files
from django.conf.urls.static import static  # Import static for serving media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('', RedirectView.as_view(url='registration/register/', permanent=False)),  # Redirect root to the registration form
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

