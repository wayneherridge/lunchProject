from django.contrib import admin

from .models import Student, Option, LunchItem

@admin.register(LunchItem)
class PostAdmin(admin.ModelAdmin):
    list_display = ['lunch_date', 'student_name', 'lunch_option', 'other_option']

# Register your models here.
admin.site.register(Student)
admin.site.register(Option)
