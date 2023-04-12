from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.home , name ='home' ),
    path('detailed/<str:id>' ,views.detailed , name = 'detailed' ),


    path('create/' ,views.createTodo , name = 'create' ),
    path('update/<str:pk>' ,views.updateTodo , name = 'update' ),
    path('delete/<str:pk>' ,views.delete , name = 'delete' ),
    
    path('signup/',views.CreateUser,name="signup"),
    
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('createItem/<str:id>' ,views.createTodoItem , name = 'createItem' ),
    path('deleteTodoItem/<str:pk>' , views.deleteTodoItem ,name='deleteTodoItem'),
    path('updateTodoItem/<str:pk>' , views.updateTodoItem ,name='updateTodoItem')
]
