from django.urls import path
from . import views
urlpatterns=[
    path("",views.apioverview,name="apioverview"),
    path("tasklist/",views.tasklist,name="tasklist"),
    path("taskdetails/<pk>/",views.taskdetails,name="taskdetails"),
    path("taskcreate/",views.taskcreate,name="taskcreate"),
    path("taskupdate/<pk>/",views.taskupdate,name="taskupdate"),
    path("taskdelete/<pk>/",views.taskdelete,name="taskdelete")
]