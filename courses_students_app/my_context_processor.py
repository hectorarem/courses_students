from django.db.models import Count
from datetime import datetime, timedelta

from courses_students_app.models import Course


def top_3_courses(context):
    months_before = 6
    now = datetime.utcnow()
    tomorrow = now + timedelta(days=1)
    from_datetime = now - timedelta(days=(months_before * 365 / 12))
    courses_lsm = Course.objects.filter(end_date__gt=from_datetime, end_date__lt=tomorrow)\
                    .annotate(total_student=Count('students')).order_by('-total_student')
    courses = Course.objects.annotate(total_student=Count('students')).order_by('-total_student')
    return {
        'top_3_courses_last_six_months': courses_lsm[:3],
        'top_3_courses': courses[:3],
    }
