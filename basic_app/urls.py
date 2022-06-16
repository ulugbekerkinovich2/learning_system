from django.urls import path

from basic_app import views

urlpatterns = [
    path('', views.index),
    path('user/', views.ListUser.as_view()),
    path('user/<int:pk>', views.DetailUser.as_view()),

    path('marks/', views.ListMarks.as_view()),
    path('marks/<int:pk>', views.DetailMarks.as_view()),
    path('student/', views.ListStudent.as_view()),
    path('student/<int:pk>', views.DetailStudent.as_view()),
    path('message/', views.ListMessage.as_view()),
    path('message/<int:pk>', views.DetailMessage.as_view()),

    path('token/', views.GetCustomToken.as_view())

]
