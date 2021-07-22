from django.conf import settings
from django.db import models


class School(models.Model):
    school_name = models.CharField(max_length=200, null=True)
    school_code = models.CharField(max_length=10)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.school_name


class Department(models.Model):

    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=10)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_code


class Courses(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_code


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    # passcode = models.CharField(max_length=100, default=unique_passcode)
    upload = models.FileField(upload_to="assignments/", null=True, default="No file uploaded")
    due_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignments"
    )

    def __str__(self):
        return self.title


class Submission(models.Model):
    matric_number = models.CharField(max_length=100)
    upload = models.FileField(upload_to="submissions/")
    submitted_at = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    assignment = models.ForeignKey(
        "Assignment", on_delete=models.CASCADE, related_name="submissions"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="submissions"
    )
    grade = models.CharField(max_length=100, null=True, blank=True, default="No grade yet")
    feedback = models.CharField(max_length=255, null=True, blank=True, default="No feedback yet")

    def __str__(self):
        return str(self.user)
