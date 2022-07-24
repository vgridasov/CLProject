from django.urls import path

from . import views

app_name = 'cytology'

urlpatterns = [
    path('list/', views.AListView.as_view(), name='list'),
    path('list/<int:pk>/', views.ADetailView.as_view(), name='detail'),
    path('<int:year>/', views.AYearArchiveView.as_view(), name='archive_year'),
    path('<int:year>/<str:month>/', views.AMonthArchiveView.as_view(), name='archive_month'),
    path('<int:year>/week/<int:week>/', views.AWeekArchiveView.as_view(), name='archive_week'),
    path('<int:year>/<str:month>/<int:day>/', views.ADayArchiveView.as_view(), name='archive_day'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('', views.IndexView.as_view(), name='home'),
]