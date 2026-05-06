from django.contrib import admin
from django.urls import path
from landpage.views import (
    landing, signin, signup, logout_view,
    dashboard, dashboard_student, dashboard_faculty, dashboard_admin,
    feed_create, chatbot, search
)

urlpatterns = [
    path('', landing, name="landing"),
    path('signin/', signin, name="signin"),
    path('signup/', signup, name="signup"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/student/', dashboard_student, name="dashboard_student"),
    path('dashboard/faculty/', dashboard_faculty, name="dashboard_faculty"),
    path('dashboard/admin/', dashboard_admin, name="dashboard_admin"),
    path('feed/create/', feed_create, name="feed_create"),
    path('chatbot/', chatbot, name="chatbot"),
    path('search/', search, name="search"),
    path('logout/', logout_view, name="logout"),
    path('admin/', admin.site.urls),
]