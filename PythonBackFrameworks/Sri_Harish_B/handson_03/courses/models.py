from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    # on_delete=CASCADE: deleting a Department deletes its Courses too —
    # keeps the DB free of orphaned rows.
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    enrollment_year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    enrollment_date = models.DateField()
    grade = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )
    
    class Meta:
        # Enforced at the DB level: a given student can only enroll in the
        # same course once (prevents duplicate enrollment rows).
        unique_together = [['student','course']]

    def __str__(self):
        return f"{self.student} - {self.course}"