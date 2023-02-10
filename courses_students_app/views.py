from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.db.models import Count
from datetime import datetime, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from courses_students_app import forms
from courses_students_app.models import Course, Student


def home(request):
    months_before = 6
    now = datetime.utcnow()
    tomorrow = now + timedelta(days=1)
    from_datetime = now - timedelta(days=(months_before * 365 / 12))
    courses_lsm = Course.objects.filter(end_date__gt=from_datetime, end_date__lt=tomorrow) \
        .annotate(total_student=Count('students')).order_by('-total_student')
    courses = Course.objects.annotate(total_student=Count('students')).order_by('-total_student')
    students = Student.objects.order_by("-pk")
    return render(request, "home.html", {
        'top_3_courses_last_six_months': courses_lsm[:3],
        'top_3_courses': courses[:3],
        'students': students[:5],
        'students_count': students.count(),
        'courses_count': Course.objects.count(),
    })


def sign_in(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        access = authenticate(username=user, password=passw)
        if access is not None:
            if access.is_active:
                login(request, access)
                messages.success(request, "Usted se ha logueado con éxito")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Usuario inactivo")
        else:
            messages.error(request, "Nombre de usuario y/o contraseña erróneo")
    return render(request, "login.html")


def logout(request):
    return logout_then_login(request, "login")


def students_list(request):
    students = Student.objects.all()
    return render(request, "courses_students_app/student/student_list.html", {"students": students})

def students_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, "courses_students_app/student/student_detail.html", {"student": student})


def student_create(request):
    if request.POST:
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante creado con éxito")
            return HttpResponseRedirect(reverse('student_list'))
        else:
            messages.error(request, "Error en el formulario")
    else:
        form = forms.StudentForm()
    args = {}
    args["form"] = form
    return render(request, "courses_students_app/student/student_form.html", args)


def courses_list(request):
    courses = Course.objects.all()
    return render(request, "courses_students_app/course/course_list.html", {"courses": courses})


def courses_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, "courses_students_app/course/course_detail.html", {"course": course})


def course_create(request):
    if request.POST:
        form = forms.CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso creado con éxito")
            return HttpResponseRedirect(reverse('courses_list'))
        else:
            messages.error(request, "Error en el formulario")
    else:
        form = forms.CourseForm()
    args = {}
    args["form"] = form
    return render(request, "courses_students_app/course/course_form.html", args)
