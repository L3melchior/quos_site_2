from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from Users.views import RequestQRList, RequestQRDetail



urlpatterns = [
    path('', views.user_login, name='login'),
    path("get_qr/", views.get_qr, name="get_qr"),
    path("home/", views.home, name="home"),
    path("error_double_use/", views.error_double_use, name="error_double_use"),
    path('RequestQRs/', RequestQRList.as_view(), name='RequestQR-list'),
    path('RequestQRs/<int:pk>/', RequestQRDetail.as_view(), name='RequestQR-detail'),
    path('scan_qr/', views.scan_qr, name='scan_qr')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
