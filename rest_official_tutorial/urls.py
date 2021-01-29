
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path('jwt/', include('jwt_auth.urls'))
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
