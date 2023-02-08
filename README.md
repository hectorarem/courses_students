# courses_students
aplicación web con estructura monolítica con Python que permita la gestión de cursos, estudiantes y la asignación entre estos, teniendo en cuenta que un estudiante puede estar asociado a varios cursos.


## Pasos para levantar el proyecto
0. Crear file `.env` en la carpeta de `courses_students` con estos parametros:
    ```
    NAME=db_name
    USER=db_user
    PASSWORD=db_password
    HOST=db_host
    PORT=db_port
    LOCAL=true
    ```
    La variable LOCAL intercambia la base de datos local SQlite con PostgreSQL online
    
1. Crear un nuevo entorno virtual:

        python3 -m venv env

2. Activar el entorno:

        source env/bin/activate

3. El entorno tiene que estar activado para el resto de los comandos.

4. Instalar las dependencias:

        pip install -r requirements.txt

5. Inicializar el servidor:

        python manage.py runserver

6. Entrar desde el navegador en http://127.0.0.1:8000

7. Usuario Admin: `angelica` Password: `zaqwsxcderfvbgtyhnmjuik`

## Descripción del ejercicio

Para ver la descripción completa del ejercicio, ir a
`docs/ejercicio.docx`

## Solución explicada

Para ver la explicación de la solucion realizada ver

`docs/solucion.docx`

## Dumpdata y loaddata

Se pueden guardar o restaurar datos usando los fixtures de django
En este caso ayuda mucho si quieres probar en diferentes bases de datos
y solo poblar una.

para realizar la salva tenemos

`python manage.py dumpdata > fixtures/whole.json`

para restaurar, primero debemos borrar los contenttypes

`python manage.py shell`

`from django.contrib.contenttypes.models import ContentType`

`ContentType.objects.all().delete()`

y despues ya ejecutamos el loaddata

 `python manage.py loaddata fixture/whole.json`