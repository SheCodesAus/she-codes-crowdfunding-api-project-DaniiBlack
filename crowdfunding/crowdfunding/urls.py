from django.urls import path, include

urlpatterns = [
    path('', include('projects.urls')),
    path('users/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('admin/', admin.site.urls),
    # path('', include('projects.urls')),
    # path('', include('users.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]
# '' empty string, we want this to be added to the homepage. So we use the 'pattern' of empty string 