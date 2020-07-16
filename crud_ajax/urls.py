

from django.urls import path,include
from . import views
from .views import ValidateUsername

urlpatterns = [
	path('list/',views.index,name="list"),
	path('update_list/<str:pk>/',views.UpdateTask,name="update_list"),
	path
	('delete_list/<str:pk>/',views.DeleteTask,name="delete_list"),
	path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.register, name="register"),
 	path('oauth/', include('social_django.urls', namespace='social')),  # <-- here
	path('ajax/validate-email/', ValidateUsername.as_view(), name='simple_ajax_validate'),
	path('book_list/',views.book_list,name="book_list"),
	path('upload_book/',views.upload_book,name="upload_book")
]
