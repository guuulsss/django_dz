from django.urls import include, path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    # path('', views.index, name='index'),
    # path('bugs/', views.bug_report_list, name='bug_report_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_report_detail, name='bug_report_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    # path('bug/new/', views.create_bug_report, name='create_bug_report'),
    # path('feature/new/', views.create_feature_request, name='create_feature_request'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugReportListView.as_view(), name='bug_report_list'),
    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_report_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
    path('bug/new/', views.create_bug_report, name='create_bug_report'),
    path('feature/new/', views.create_feature_request, name='create_feature_request'),

]
