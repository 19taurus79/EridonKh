"""
URL configuration for djangoProjectKh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("EridonKh.urls")),
    # path("", SubmissionsView.as_view(), name="home_page"),
    # path("login/", user_login, name="user_login"),
    # path("logout/", user_logout, name="user_logout"),
    path("admin/", admin.site.urls, name="admin"),
    # path("filter/", RemainsFiltered.as_view(), name="remains_filtered"),
    # path("remains/", RemainsView.as_view(), name="remains_page"),
] + debug_toolbar_urls()
