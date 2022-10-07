from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View
from rest_framework.viewsets import ModelViewSet


from course.models import  Course, Module, Content
from course.serializers import CourseSerializer, ModuleSerializer, ContentSerializer
# Create your views here.



class CourseViewset(ModelViewSet):

    queryset =  Course.objects.all()
    serializer_class = CourseSerializer

   

    def get_serializer_context(self):
        return {'request': self.request}

    # def destroy(self, request, *args, **kwargs):
    #     if OrderItem.objects.filter(product_id=kwargs['pk']).count()>0:
    #         return Response('error')

    #     return super().destroy(request, *args, **kwargs)

class ModuleViewset(ModelViewSet):
    serializer_class = ModuleSerializer

    def get_queryset(self):
        return Module.objects.filter(course_id = self.kwargs['course_pk'])
        

    def get_serializer_context(self):
        return {'course_id':self.kwargs['course_pk']}

class ContentViewset(ModelViewSet):
    serializer_class = ContentSerializer

    def get_queryset(self):
        return Content.objects.filter(module_id = self.kwargs['course_module_pk'])
        

    def get_serializer_context(self):
        return {'module_id':self.kwargs['course_module_pk']}
