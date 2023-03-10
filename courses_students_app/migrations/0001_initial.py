# Generated by Django 4.1.2 on 2023-02-07 21:41

import courses_students_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, validators=[courses_students_app.validators.validate_name], verbose_name='Nombre')),
                ('lastname', models.CharField(max_length=255, validators=[courses_students_app.validators.validate_name], verbose_name='Apellidos')),
                ('age', models.IntegerField(validators=[courses_students_app.validators.validate_age], verbose_name='Edad')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('schedule', models.CharField(max_length=255, verbose_name='Horario')),
                ('start_date', models.DateTimeField(verbose_name='Fecha inicio')),
                ('end_date', models.DateTimeField(verbose_name='Fecha fin')),
                ('students', models.ManyToManyField(to='courses_students_app.student', verbose_name='Estudiantes')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ('start_date',),
            },
        ),
    ]
