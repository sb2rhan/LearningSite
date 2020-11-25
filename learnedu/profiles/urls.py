from django.urls import path
from profiles import views


urlpatterns = [
    path('<slug:username>', views.profile_page, name='profile_page'),
    path('<slug:username>/posts/create', views.create_post, name="create_post"),
    path('<slug:username>/posts/delete/<int:id>', views.delete_post, name="delete_post"),
    path('<slug:username>/edit', views.edit_profile, name="edit_profile"),
    path('<slug:username>/courses', views.courses_page, name="courses_page"),
    path('<slug:username>/courses/<int:id>', views.course_detail, name="course_detail"),
    path('<slug:username>/courses/<int:id>/enroll', views.course_enroll, name="course_enroll"),
    path('<slug:username>/courses/<int:id>/unenroll', views.course_unenroll, name="course_unenroll"),
    path('<slug:username>/courses/<int:id>/delete', views.course_delete, name="course_delete"),
    path('<slug:username>/courses/create', views.create_course, name="create_course"),
]
