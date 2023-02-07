from django.db import models

from courses_students_app.validators import validate_name, validate_age


class Student(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=255, validators=[validate_name])
    lastname = models.CharField(verbose_name="Apellidos", max_length=255, validators=[validate_name])
    age = models.IntegerField(verbose_name="Edad", validators=[validate_age])
    email = models.EmailField(verbose_name="Correo electrónico", max_length=254)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ('name',)

    def __str__(self):
        return f"{self.name} - {self.lastname}"

    def assosiates_courses(self):
        return " || ".join([c.name for c in self.course_set.all()])


class Course(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=255)
    schedule = models.CharField(verbose_name="Horario", max_length=255)
    start_date = models.DateTimeField(verbose_name="Fecha inicio")
    end_date = models.DateTimeField(verbose_name="Fecha fin")
    students = models.ManyToManyField(Student, verbose_name="Estudiantes")

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('start_date',)

    def __str__(self):
        return f"{self.name} ({self.schedule})"

    def number_associates_students(self):
        return self.students.all().count()




