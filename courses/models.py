from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    coach = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class CourseSlot(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.name} - {self.start_datetime}"



class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(CourseSlot, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'slot')  # une inscription unique par cours

    def __str__(self):
        return f"{self.user.username} - {self.slot}"

