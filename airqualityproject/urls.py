from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views
from data.views import CityListView
from plants.views import PlantListView
from vehicles.views import VehicleListView
from data import views as data_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register/', user_views.register, name='register'),
	path('profile/', user_views.profile, name='profile'),
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('forum.urls')),
    path('cities/', CityListView.as_view(), name='cities'),
    path('plants/', PlantListView.as_view(), name='plants'),
    path('vehicles/', VehicleListView.as_view(), name='vehicles'),
    path('charts/pie-chart1', data_views.pie_chart1, name='pie-chart1'),
    path('charts/pie-chart2', data_views.pie_chart2, name='pie-chart2'),
    path('charts/line-chart1', data_views.line_chart1, name='line-chart1'),
    path('charts/line-chart2', data_views.line_chart2, name='line-chart2'),
    path('charts/bar-chart1', data_views.bar_chart1, name='bar-chart1'),
    path('charts/bar-chart2', data_views.bar_chart2, name='bar-chart2'),
    path('charts/box-plot1', data_views.box_plot1, name='box-plot1'),
    path('charts/', data_views.charts, name='charts'),
    ]
