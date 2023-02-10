from django import forms
from django.contrib import messages
from django.forms import widgets
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from courses_students_app import models


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ("name", "lastname", "age", "email")
        widgets = {
            "name": widgets.TextInput(attrs={"class": " form-control"}),
            "lastname": widgets.TextInput(attrs={"class": " form-control"}),
            "age": widgets.NumberInput(attrs={"class": " form-control"}),
            "email": widgets.EmailInput(attrs={"class": " form-control"}),
        }


class StudentUpdate(UpdateView):
    form_class = StudentForm
    model = models.Student
    success_url = reverse_lazy("student_list")
    template_name = 'courses_students_app/student/student_form.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, "Estudiante modificado con éxito")
        return super(StudentUpdate, self).post(request, *args, **kwargs)


class StudentDelete(DeleteView):
    model = models.Student
    success_url = reverse_lazy("student_list")
    template_name = 'courses_students_app/student/student_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Estudiante eliminado con éxito")
        return HttpResponseRedirect(success_url)


class CourseForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ("name", "schedule", "start_date", "end_date", "students")
        widgets = {
            "name": widgets.TextInput(attrs={"class": " form-control"}),
            "schedule": widgets.Select(attrs={"class": " form-control"}),
            "start_date": widgets.SelectDateWidget(attrs={"class": " form-control", "type": "date"}),
            "end_date": widgets.SelectDateWidget(attrs={"class": " form-control", "type": "date"}),
            "students": widgets.SelectMultiple(attrs={"class": " form-control select2"})
        }


class CourseUpdate(UpdateView):
    form_class = CourseForm
    model = models.Course
    success_url = reverse_lazy("courses_list")
    template_name = 'courses_students_app/course/course_form.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, "Curso modificado con éxito")
        return super(CourseUpdate, self).post(request, *args, **kwargs)


class CourseDelete(DeleteView):
    model = models.Course
    success_url = reverse_lazy("courses_list")
    template_name = 'courses_students_app/course/course_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(request, "Curso eliminado con éxito")
        return HttpResponseRedirect(success_url)
