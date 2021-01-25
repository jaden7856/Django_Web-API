from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import rest_views

from mysite.views import HomeView


router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='index'),
    path('', HomeView.as_view(), name='home'),
    
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    
    path('blog/', include('blog.urls', namespace='blog')),

    path('api/', include('api.urls', namespace='api'))

    # path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]
