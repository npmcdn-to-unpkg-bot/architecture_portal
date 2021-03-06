"""architecture_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from enduser_app import views

urlpatterns = [
    url(r'^$', views.index, name='enduser_index'),
    url(r'^operations/$', views.operations, name='enduser_operations'),
    url(r'^instances/$', views.instances, name='enduser_instances'),
    url(r'^instances/foroperation/(?P<operation_id>[0-9]+)/$',
        views.instances_operation, name='enduser_instances_operation'),
    url(r'^executions/$', views.executions, name='enduser_executions'),
    url(r'^run_execution/(?P<execution_id>[0-9]+)/$',
        views.run_execution, name='enduser_run_execution'),
    url(r'^instance_form/$', views.instance_form, name='enduser_instance_form'),
    url(r'^instance_post/$', views.instance_post, name='enduser_instance_post'),
    url(r'^execution_form/$', views.execution_form, name='enduser_execution_form'),
    url(r'^execution_post/$', views.execution_post, name='enduser_execution_post'),
    url(r'^clusters/$', views.clusters, name='enduser_clusters'),
]
