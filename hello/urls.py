from django.urls import path
from . import views

app_name='hello'

urlpatterns = [
    path('',views.get_index_page, name='index_page'),
    path('research/',views.get_research_page, name='research_page'),
    path('teaching/',views.get_teaching_page, name='teaching_page'),
    path('blog/',views.get_blog_page, name='blog_page'),
    # path('bibliography/', views.get_bibliography, name='biblography_page'),
    # path('grades/<str:filename>', views.get_student_result, name='student_result'),
    # path('logout', views.get_logout_page, name='logout_page'),
]