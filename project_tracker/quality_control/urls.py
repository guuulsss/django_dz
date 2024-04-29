from django.urls import include, path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),
    # path('bugs/', views.bug_report_list, name='bug_report_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_report_detail, name='bug_report_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    # path('bug/new/', views.create_bug_report, name='create_bug_report'),
    # path('feature/new/', views.create_feature_request, name='create_feature_request'),
    # path('bug/<int:bug_id>/update/', views.update_bug, name='update_bug'),
    # path('feature/<int:feature_id>/update/', views.update_feature, name='update_feature'),
    # path('bug/<int:bug_id>/delete/', views.delete_bug, name='delete_bug'),
    # path('feature/<int:feature_id>/delete/', views.delete_feature, name='delete_feature'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugReportListView.as_view(), name='bug_report_list'),
    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugReportDetailView.as_view(), name='bug_report_detail'),
    path('features/<int:feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_detail'),
    path('bug/create/', views.BugReportCreateView.as_view(), name='create_bug_report'),
    path('feature/create/', views.FeatureRequestCreateView.as_view(), name='create_feature_request'),
    path('bug/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='update_bug'),
    path('feature/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='update_feature'),
    path('bug/<int:bug_id>/delete/', views.BugReportDeleteView.as_view(), name='delete_bug'),
    path('feature/<int:feature_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),

]
