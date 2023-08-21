from django.shortcuts import render
from CRUDOperation.models import StuModel
from django.contrib import messages
from django.http import HttpResponse
from CRUDOperation.forms import Stuforms
from django.db import connection

def showemp(request):
    showall=StuModel.objects.all()
    return render(request,'Index.html',{"data":showall})

def InsertStu(request):
    if request.method=="POST":
        if request.POST.get('Student_Id') and request.POST.get('Student_name') and request.POST.get('Students_branch') and request.POST.get('academic_year'):
            saverecord=StuModel()
            saverecord.Student_Id= request.POST.get('Student_Id')
            saverecord.Student_name= request.POST.get('Student_name')
            saverecord.Students_branch= request.POST.get('Students_branch')
            saverecord.Academic_year= request.POST.get('academic_year')
            saverecord.save()
        messages.success(request,'Student ' +saverecord.Student_name+ ' is Saved successfully..!')
        return render(request,'Insert.html')
    else:
        return render(request,'Insert.html')

def EditStu(request,id):
    editStuobj=StuModel.objects.get(Student_Id=id)
    return render(request,'Edit.html',{"StuModel":editStuobj})

def UpdateStu(request,id):
    UpdateStu=StuModel.objects.get(Student_Id=id)
    form=Stuforms(request.POST,instance=UpdateStu)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully..!')
        return render(request,'Edit.html',{"StuModel":UpdateStu})

def DelStu(request,id):
    delStu=StuModel.objects.get(Student_Id=id)
    delStu.delete()
    showdata=StuModel.objects.all()
    return render(request,"Index.html",{"data":showdata})

def Homepage(request):
    return render(request,'Homepage.html')

def runQuery(request):
    raw_query = "select * from student where academic_year=2020"

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata=cursor.fetchall()

    return render(request,'runQuery.html',{'data':alldata})