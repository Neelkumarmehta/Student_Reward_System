from django.db import models

class StuModel(models.Model):
    Student_Id=models.IntegerField(primary_key=True)
    Student_name=models.CharField(max_length=300)
    Students_branch=models.CharField(max_length=300)
    academic_year=models.IntegerField()
    class Meta:
        db_table='student'