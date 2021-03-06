from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    path(_(''), views.index, name='index'),
    path('about/', views.about, name='about'),
    path('internet/', views.internet, name='internet'),
    path('speedtest/', views.speedtest, name='speedtest'),
    path('blog/', views.blog, name='blog'),
    path('singl-blog/<str:pk>', views.singl_blog, name='single-blog'),
    path('contact/', views.contact, name='contact'),
    path('docs/', views.docs, name='docs'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('requests_t0_admin_new/', views.requests_t0_admin_new, name='requests_t0_admin_new'),
    path('requests_t0_admin_done/', views.requests_t0_admin_done, name='requests_t0_admin_done'),
    path('request_edit/<str:pk>', views.request_edit, name='request_edit'),
]