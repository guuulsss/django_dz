from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from tasks.models import Project, Task
from quality_control.models import BugReport, FeatureRequest
from django.shortcuts import render, get_object_or_404, redirect

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
    bug_report_list = BugReport.objects.all()
    return render(request, 'quality_control/bug_report_list.html', {'bug_report_list': bug_report_list})

# def bug_report_list(request):
#     bug_reports = BugReport.objects.all()
#     html = '<h1>Список всех Багов</h1>'
#     for bug_report in bug_reports:
#         html += f'<li><a href="{bug_report.id}/">{bug_report.title}</a></li>'
#     return HttpResponse(html)
def bug_report_detail(request, bug_id):
    bug_reports = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_report_detail.html', {'bug_report_list': bug_reports})

from django.shortcuts import redirect
from .forms import BugReportForm

def create_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_report_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_create.html', {'form': form})

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
from .forms import FeatureRequestForm
def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_create.html', {'form': form})

def update_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_report_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'features': feature})

def delete_bug(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    bug.delete()
    return redirect('quality_control:bug_report_list')

def delete_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list', feature_id=feature_id)

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#
#         bugs_url = reverse('quality_control:bug_report_list')
#         features_url = reverse('quality_control:feature_list')
#         html = f"<h1>Система контроля качества</h1>"
#         html += f"<a href='{bugs_url}'>Список всех багов</a>"
#         html += f"<br><a href='{features_url}'>Запросы на улучшение</a>"
#         return HttpResponse(html)

from django.views.generic import ListView

class BugReportListView(ListView):

    model = BugReport
    template_name = 'quality_control/bug_report_list.html'
    context_object_name = 'bug_report_list'


# class BugReportListView(ListView):
#
#     model = BugReport
#
#     def get(self, request, *args, **kwargs):
#         bug_reports = self.get_queryset()
#         bug_reports_html = '<h1>Список багов</h1>'
#
#         for bug_report in bug_reports:
#             bug_reports_html += f'<li><a href="{bug_report.id}/">{bug_report.title}</a></li>'
#
#         bug_reports_html += '</ul>'
#
#         # Возвращаем HTML-код как HttpResponse
#         return HttpResponse(bug_reports_html)


from django.views.generic import DetailView

class BugReportDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_report_detail.html'
    context_object_name = 'bug_report_list'

# class BugReportDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         bug_report = self.object
#         response_html = f'<h1>{bug_report.title}</h1>'
#         response_html += f'<p>Status: {bug_report.status}</p>'
#         response_html += f'<p>Description: {bug_report.description}</p>'
#         response_html += f'<p>Project: {bug_report.project.name}</p>'
#         response_html += f'<p>Task: {bug_report.task.name}</p>'
#         return HttpResponse(response_html)


class FeatureRequestListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'
    context_object_name = 'features'
# class FeatureRequestListView(ListView):
#     model = FeatureRequest
#
#     def get(self, request, *args, **kwargs):
#         features = self.get_queryset()
#         features_html = '<h1>Список багов</h1>'
#
#         features_html = '<h1>Список всех Запросов на улучшение</h1>'
#         for feature in features:
#             features_html += f'<li><a href="{feature.id}/">{feature.title}</a></li>'
#         return HttpResponse(features_html)
class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'features'
    template_name = 'quality_control/feature_detail.html'


# class FeatureRequestDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         feature = self.object
#         response_html = f'<h1>{feature.title}</h1>'
#         response_html += f'<p>Status: {feature.status}</p>'
#         response_html += f'<p>Priority: {feature.priority}</p>'
#         response_html += f'<p>Description: {feature.description}</p>'
#         response_html += f'<p>Project: {feature.project.name}</p>'
#         response_html += f'<p>Task: {feature.task.name}</p>'
#         return HttpResponse(response_html)

from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_create.html'
    success_url = reverse_lazy('quality_control:bug_report_list')


from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

class FeatureRequestCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_create.html'
    success_url = reverse_lazy('quality_control:feature_list')

from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('quality_control:bug_report_list')

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('quality_control:feature_list')

from django.views.generic.edit import DeleteView

class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug_report_list'
    success_url = reverse_lazy('quality_control:bug_report_list')
    template_name = 'quality_control/bug_confirm_delete.html'

from django.views.generic.edit import DeleteView

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'features'
    success_url = reverse_lazy('quality_control:feature_list')
    template_name = 'quality_control/feature_confirm_delete.html'
