from rest_framework import serializers
from course.models import Course, Module, Content

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'created_at', 'last_updated']


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        fields = ['id', 'module_title', 'description']

    def create(self, validated_data):
        course_id = self.context['course_id']

        return Module.objects.create(course_id = course_id, **validated_data)

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = ['id', 'content_title', 'content']

    def create(self, validated_data):
        module_id = self.context['module_id']

        return Content.objects.create(module_id = module_id, **validated_data)






