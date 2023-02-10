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
        return f"{self.name} {self.lastname}"

    def full_info(self):
        return self.__str__() + f" || Edad: {self.age} || Email: {self.email}"

    def cursos_asociados(self):
        return " <br> ".join([c.name for c in self.course_set.all()])


class Course(models.Model):
    SCHEDULE_LIST = (
        ("9_11", '9:00 AM - 11:00 AM',),
        ("11_13", '11:00 AM - 1:00 PM',),
        ("13_15", '1:00 PM - 3:00 PM',),
        ("15_17", '3:00 PM - 5:00 PM',),
        ("17_19", '5:00 PM - 7:00 PM',),
        ("19_21", '7:00 PM - 9:00 PM',),
    )
    name = models.CharField(verbose_name="Nombre", max_length=255)
    schedule = models.CharField(verbose_name="Horario", max_length=255, choices=SCHEDULE_LIST)
    start_date = models.DateTimeField(verbose_name="Fecha inicio")
    end_date = models.DateTimeField(verbose_name="Fecha fin")
    students = models.ManyToManyField(Student, verbose_name="Estudiantes", blank=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ('start_date',)

    def __str__(self):
        return f"{self.name} ({self.get_schedule_display()})"

    def numeros_de_estudiantes_asociados(self):
        return self.students.all().count()




