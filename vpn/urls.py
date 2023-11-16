from django.urls import path

from . import views

urlpatterns = [
    path('sites/', views.SitesPage.as_view(), name='sites'),
    path('sites/delete/<int:pk>/', views.SiteDelete.as_view(), name='site_delete'),
    path('statistics/', views.StatisticsPage.as_view(), name='statistics'),
    path('<str:site_name>/', views.vpn_page, name='vpn_page'),
    path('<str:site_name>/<path:site_path>/', views.vpn_page, name='vpn_path'),
]
