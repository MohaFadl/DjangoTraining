from django.contrib import admin
from courses.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'instructor', 'price', 'start_date')
    search_fields = ('course_code', 'title', 'instructor')
    list_filter = ('start_date',)
