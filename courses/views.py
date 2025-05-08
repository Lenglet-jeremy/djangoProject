from django.shortcuts import render
from .models import CourseSlot
from datetime import datetime

def upcoming_courses(request):
    slots = CourseSlot.objects.filter(start_datetime__gte=datetime.now()).order_by('start_datetime')
    return render(request, 'courses/upcoming.html', {'slots': slots})

