from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def student_detail(request,pk):

    length = Student.objects.count()
    if pk > length:
        return HttpResponse("Data not found for current query, try to change and check")
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    print(type(serializer.data))
    json_data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_data, content_type='application/json')

def student_list(request):
    stu = Student.objects.all()

    serializer = StudentSerializer(stu, many=True)
    print(type(serializer.data))
    return JsonResponse(serializer.data, safe=False)