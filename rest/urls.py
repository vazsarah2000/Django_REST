from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('student/',studentAPI.as_view()),
    path('register/',registerUser.as_view())

    
]

"""path('post/',post_data),
    path('update/<id>/',update_data),
    path('delete/<id>/',delete_data)
    """