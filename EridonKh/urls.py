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

from django.urls import path
from EridonKh import views

urlpatterns = [
    # path(
    #     "submissions/<str:sub_client>/",
    #     views.submissions_detail,
    #     name="submissions_detail",
    # ),
    path("", views.SubmissionsClientView.as_view(), name="home_page"),
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("filter/", views.RemainsFiltered.as_view(), name="remains_filtered"),
    path("remains/", views.RemainsView.as_view(), name="remains_page"),
    path(
        "submissions/<uuid:client>",
        views.submissions_number_detail,
        name="submissions",
    ),
    path(
        "submissions/<uuid:client>/<uuid:cont_sub>",
        views.submissions_prod_details,
        name="submissions_prod",
    ),
    path(
        "submissions_filtered/",
        views.submissions_manager,
        name="submissions_manager",
    ),
]
