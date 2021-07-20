from django.db import models
from django.contrib.auth.models import AbstractUser
from assignments.models import School, Department, Courses


level_choices = (
    ("100", "100"),
    ("200", "200"),
    ("300", "300"),
    ("400", "400"),
    ("500", "500"),
)

alias_choice = (("Mr.", "Mr."), ("Mrs", "Mrs"), ("Dr.", "Dr."), ("Prof.", "Prof."))

gender_choices = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    alias = models.CharField(choices=alias_choice, max_length=5, null=True)
    level = models.CharField(choices=level_choices, max_length=11, null=True, blank=True)
    gender = models.CharField(choices=gender_choices, max_length=6)
    courses = models.ManyToManyField(Courses, blank=True)