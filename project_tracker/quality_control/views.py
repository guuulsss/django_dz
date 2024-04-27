from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from tasks.models import Project, Task
from quality_control.models import BugReport, FeatureRequest
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,'quality_control/index.html')
# def index(request):
#     bugs_url = reverse('quality_control:bug_report_list')
#     features_url = reverse('quality_control:feature_list')
#     html = f"<h1>Система контроля качества</h1>"
#     html += f"<a href='{bugs_url}'>Список всех багов</a>"
#     html += f"<br><a href='{features_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

def bug_report_list(request):
    bug_reports = BugReport.objects.all()
    return render(request, 'quality_control/bug_report_list.html', {'bug_report_list': bug_reports})

# def bug_report_list(request):
#     bug_reports = BugReport.objects.all()
#     html = '<h1>Список всех Багов</h1>'
#     for bug_report in bug_reports:
#         html += f'<li><a href="{bug_report.id}/">{bug_report.title}</a></li>'
#     return HttpResponse(html)
def bug_report_detail(request, bug_id):
    bug_reports = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_report_detail.html', {'bug_report_list': bug_reports})

# def bug_report_detail(request, bug_id):
#     bug_report = get_object_or_404(BugReport, id=bug_id)
#     response_html = f'<h1>{bug_report.title}</h1>'
#     response_html += f'<p>Status: {bug_report.status}</p>'
#     response_html += f'<p>Description: {bug_report.description}</p>'
#     return HttpResponse(response_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': features})

# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     html = '<h1>Список всех Запросов на улучшение</h1>'
#     for feature in features:
#         html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
#     return HttpResponse(html)

def feature_detail(request, feature_id):
    features = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'features': features})

# def feature_detail(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, id=feature_id)
#     response_html = f'<h1>{feature.title}</h1>'
#     response_html += f'<p>Status: {feature.status}</p>'
#     response_html += f'<p>Priority: {feature.priority}</p>'
#     response_html += f'<p>Description: {feature.description}</p>'
#     return HttpResponse(response_html)

#def quality_control_index(request):
#    return HttpResponse("<h1>Главная страница приложения quality_control</h1>")

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):

        bugs_url = reverse('quality_control:bug_report_list')
        features_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1>"
        html += f"<a href='{bugs_url}'>Список всех багов</a>"
        html += f"<br><a href='{features_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)

from django.views.generic import ListView


class BugReportListView(ListView):

    model = BugReport

    def get(self, request, *args, **kwargs):
        bug_reports = self.get_queryset()
        bug_reports_html = '<h1>Список багов</h1>'

        for bug_report in bug_reports:
            bug_reports_html += f'<li><a href="{bug_report.id}/">{bug_report.title}</a></li>'

        bug_reports_html += '</ul>'

        # Возвращаем HTML-код как HttpResponse
        return HttpResponse(bug_reports_html)


from django.views.generic import DetailView

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug_report = self.object
        response_html = f'<h1>{bug_report.title}</h1>'
        response_html += f'<p>Status: {bug_report.status}</p>'
        response_html += f'<p>Description: {bug_report.description}</p>'
        response_html += f'<p>Project: {bug_report.project.name}</p>'
        response_html += f'<p>Task: {bug_report.task.name}</p>'
        return HttpResponse(response_html)


class FeatureRequestListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = '<h1>Список багов</h1>'

        features_html = '<h1>Список всех Запросов на улучшение</h1>'
        for feature in features:
            features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
        return HttpResponse(features_html)


class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1>'
        response_html += f'<p>Status: {feature.status}</p>'
        response_html += f'<p>Priority: {feature.priority}</p>'
        response_html += f'<p>Description: {feature.description}</p>'
        response_html += f'<p>Project: {feature.project.name}</p>'
        response_html += f'<p>Task: {feature.task.name}</p>'
        return HttpResponse(response_html)