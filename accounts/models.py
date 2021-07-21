import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from assignments.models import Courses, Department, School

level_choices = (
    ("100L", "100L"),
    ("200L", "200L"),
    ("300L", "300L"),
    ("400L", "400L"),
    ("500L", "500L"),
)

alias_choice = (("Mr.", "Mr."), ("Mrs", "Mrs"), ("Dr.", "Dr."), ("Prof.", "Prof."))

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    alias = models.CharField(choices=alias_choice, max_length=5, null=True, blank=True)
    level = models.CharField(choices=level_choices, max_length=11, null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=6)
    courses = models.ManyToManyField(Courses, blank=True)

    def __str__(self):
        return str(self.id)
