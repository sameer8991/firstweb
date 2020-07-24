from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
#from sendfile.views import sen_file
urlpatterns = [
	path('',views.index, name='home'),
	path('search/',views.search, name='search'),
	path('sample/',views.sample, name='sample'),
	path('blog/',views.blog, name='blog'),
	path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
	path('sign/',views.sign, name='sign'),
	path("products/<int:myid>",views.bookView, name="review"),
	url(r'^view-pdf/$', views.pdf_view, name='pdf_view')


    ]