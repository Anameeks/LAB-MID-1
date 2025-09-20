from django.contrib import admin
from django.db.models import Count
from .models import Student, Instructor, Course, Enrollment


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'enrollment_date')
    search_fields = ('name',)
    list_filter = ('department',)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'credits', 'instructor', 'enrolled_students_count')
    inlines = [EnrollmentInline]

    def enrolled_students_count(self, obj):
        return Enrollment.objects.filter(course=obj).count()
    enrolled_students_count.short_description = 'Enrolled Students'


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'hire_date', 'course_count')

    def course_count(self, obj):
        return Course.objects.filter(instructor=obj).count()
    course_count.short_description = 'Number of Courses'


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'grade')

admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)

admin.site.register(Enrollment, EnrollmentAdmin)
