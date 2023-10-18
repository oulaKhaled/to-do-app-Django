from django.urls import path

from rest_framework import routers
from .views import (
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    DeleteTask,
    CustomLoginView,
    RegisterPage,
)
from django.conf.urls import include
from django.contrib.auth.views import LogoutView

# router = routers.DefaultRouter()
# router.register("task", TaskViewSet)
# router.register("user", UserViewSet)


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),
    path("", TaskList.as_view(), name="tasks"),
    path("<int:pk>/", TaskDetail.as_view(), name="task"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", DeleteTask.as_view(), name="delete-task"),
]
