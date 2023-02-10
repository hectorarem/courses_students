"""courses_students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls.static import static
from courses_students_app import views, forms
from django.conf import settings

admin.site.site_header = 'NativeApp Test'
admin.site.site_title = 'NativeApp Test'
admin.site.index_title = 'NativeApp Test'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login_required(views.home), name="home"),
    path("login/", views.sign_in, name="login"),
    path("accounts/login/", views.sign_in, name="login"),
    path("logout/", views.logout, name="logout"),
    # student CRUD
    path("students/", login_required(views.students_list), name="student_list"),
    path("students/create", login_required(views.student_create), name="student_create"),
    path("students/update/<int:pk>", login_required(forms.StudentUpdate.as_view()), name="student_update"),
    path("students/delete/<int:pk>/", login_required(forms.StudentDelete.as_view()), name="student_delete"),
    path("students/detail/<int:pk>/", login_required(views.students_detail), name="student_detail"),
    # courses CRUD
    path("courses/", login_required(views.courses_list), name="courses_list"),
    path("courses/create", login_required(views.course_create), name="courses_create"),
    path("courses/update/<int:pk>", login_required(forms.CourseUpdate.as_view()), name="courses_update"),
    path("courses/delete/<int:pk>/", login_required(forms.CourseDelete.as_view()), name="courses_delete"),
    path("courses/detail/<int:pk>/", login_required(views.courses_detail), name="courses_detail"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)