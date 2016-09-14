from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^new/(?P<lesson_id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$', views.new_student, name='new_student'),
]
