from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include

from .views import *
from . import views
from rest_framework_nested import routers



router = routers.DefaultRouter()
router.register('courses', views.CourseViewset)
## generates:
# /courses/ 
# /courses/{pk}/

modules_router = routers.NestedDefaultRouter(router, 'courses',lookup = 'course')
modules_router.register('modules',views.ModuleViewset,basename = 'course_modules')
## generates:
# /courses/{courses_pk}/modules/
# /courses/{courses_pk}/modules/{pk}/

content_router = routers.NestedDefaultRouter(modules_router, 'modules',lookup = 'course_module')
content_router.register('contents',views.ContentViewset,basename = 'module_contents')
## generates:
# /courses/{courses_pk}/modules/{module_pk}/contents/
# /courses/{courses_pk}/modules/{module_pk}/contents/{pk}/

urlpatterns = router.urls + modules_router.urls + content_router.urls






    

