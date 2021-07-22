from django.contrib import admin

from . import models


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "due_date")


@admin.register(models.Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ("course_name", "course_code", "date_time_created")


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("department_name", "department_code", "date_time_created")


@admin.register(models.School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("school_name", "school_code", "date_time_created")


admin.site.register(models.Assignment, AssignmentAdmin)
