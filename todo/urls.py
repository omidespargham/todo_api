from django.urls import path
from . import views


app_name = 'todo'

urlpatterns = [
    path("showall/",views.ShowTodosView.as_view(),name="show_todos"),
    path("create/",views.CreateTodoView.as_view(),name="create_todo"),
    # path("todo/",views.TodoCreateListView.as_view(),name="todo"), # post and get ListCreateAPI
    path("specific/<int:pk>/",views.TodoRetriveView.as_view(),name="specific_todo"),
    path("delete/<int:pk>/",views.TodoDeleteView.as_view(),name="delete_todo"),
    path("update/<int:pk>/",views.TodoUpdateView.as_view(),name="update_todo"),
    path("session/",views.GetSessionData.as_view(),name="session"),
]



