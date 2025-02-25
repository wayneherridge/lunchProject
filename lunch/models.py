from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return self.student_name

class Option(models.Model):
    option_id = models.AutoField(primary_key=True)
    option = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.option

class LunchItem(models.Model):
    lunch_item_id = models.AutoField(primary_key=True)
    lunch_date = models.DateField(auto_now_add=True)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True, related_name='student')
    lunch_option = models.ForeignKey(Option, on_delete=models.CASCADE, blank=True, null=True)
    other_option = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-student_name']


    def __str__(self):
        return f"{self.lunch_date} - {self.student_name} - {self.lunch_option} {self.other_option}"


