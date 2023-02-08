from django.contrib import admin, messages

from courses_students_app.models import Student, Course


class StudentAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'lastname', 'age', 'cursos_asociados')
    list_display_links = ("email",)
    list_editable = ('name', 'lastname', 'age',)
    search_fields = ("name", "lastname")
    list_filter = ('course',)
    list_per_page = 25

    class Meta:
        model = Student


admin.site.register(Student, StudentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'schedule', 'start_date', 'end_date', 'numeros_de_estudiantes_asociados')
    list_display_links = ("pk",)
    list_editable = ('name', 'schedule', 'start_date', 'end_date')
    search_fields = ("name", "schedule")
    list_per_page = 25

    class Meta:
        model = Course

    def save_model(self, request, obj, form, change):
        if obj.start_date < obj.end_date:
            super().save_model(request, obj, form, change)
        else:
            messages.error(request, "La fecha de inicio no puede ser posterior a la fecha fin.")


admin.site.register(Course, CourseAdmin)
