from django.contrib import admin
from django.urls import path
from myBlog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name='home'),
    path('about/', views.about ,name='about'),
    path('contact/', views.contact ,name='contact'),
    path('login/', views.login ,name='login'),
    path('logout/', views.logout ,name='logout'),
    path('signup/', views.signup ,name='signup'),
    path('dashboard/', views.dashboard ,name='dashboard'),
]
