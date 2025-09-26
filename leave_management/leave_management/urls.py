from django.contrib import admin
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # users app ke sare urls
    path('', include('users.urls')),

    # leaves app ke urls
    path('leaves/', include('leaves.urls')),
]