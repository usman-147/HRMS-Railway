"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from App.views import *
from App.models import *

from django.views.generic.base    import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path("thetribalchief/", admin.site.urls),
    path("", index, name="index"),

    path(
        "favicon.ico",
        RedirectView.as_view(
            url=staticfiles_storage.url("favicon.ico")
        )
    ),
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^Authority^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    path("authority-register/", authority_register, name="authority-register"),
    path("authority-login/", authority_login, name="authority-login"),
    path("authority-display", authority_display, name="authority-display"),
    path("authority-status", update_status, name="authority-status"),
    path("create-hr/", create_hr, name="create-hr"),

    #^^^^^^^^^^^^^^^^^^^^^^^HR^^^^^^^^^^^^^^^^^^^^^^^^^^

    path("hr-login/", hr_login, name="hr-login"),
    path("hr-display", hr_display, name="hr-display"),
    path("hr-insert", hr_insert, name="hr-insert"),
    path("search", search, name="search"),
    path("edit/<id>", edit, name="edit"),
    path("delete/<id>", delete_data, name="delete"),

    #^^^^^^^^^^^^^^^^^^^^^^^Future Iterations^^^^^^^^^^^^^^^^^^^^^^^^^^

    path("faculty-insert", faculty_insert, name="faculty-insert"),
    path("faculty-edit/<id>", faculty_edit, name="faculty-edit"),
    path("faculty-delete/<id>", faculty_delete, name="faculty-delete"),
]
