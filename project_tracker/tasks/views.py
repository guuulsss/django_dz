from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    return render(request, 'tasks/index.html')

# def index(request):
#     projects_list_url = reverse('tasks:projects_list')
#     quality_control_index_url = reverse('quality_control:index')
#     html = f"<h1>Страница приложения tasks</h1>"
#     html += f"<a href='{projects_list_url}'>Список проектов</a>"
#     html += f"<br><a href='{quality_control_index_url}'>Перейти на главную страницу приложения quality_control</a>"
#     return HttpResponse(html)


def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})

# def projects_list(request):
#     projects = Project.objects.all()
#     projects_html = '<h1>Список проектов</h1><ul>'
#     for project in projects:
#         projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#     projects_html += '</ul>'
#     return HttpResponse(projects_html)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'tasks/project_detail.html', {'project': project})

# def project_detail(request, project_id):
#     project = get_object_or_404(Project, id=project_id)
#     tasks = project.tasks.all()
#     response_html = f'<h1>{project.name}</h1><p>{project.description}</p>'
#     response_html += '<h2>Задачи</h2><ul>'
#     for task in tasks:
#         response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
#     response_html += '</ul>'
#     return HttpResponse(response_html)


from .forms import FeedbackForm
from django.core.mail import send_mail


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['info@example.com']
            recipients.append(email)

            send_mail(subject, message, email, recipients)

            return redirect('/tasks')
    else:
        form = FeedbackForm()
    return render(request, 'tasks/feedback.html', {'form': form})

from .forms import ProjectForm

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:projects_list')
    else:
        form = ProjectForm()
    return render(request, 'tasks/project_create.html', {'form': form})

from .forms import TaskForm

def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('tasks:project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})

def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, id=task_id, project_id=project_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

# def task_detail(request, project_id, task_id):
#     project = get_object_or_404(Project, id=project_id)
#     task = get_object_or_404(Task, id=task_id, project=project)
#     response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
#     return HttpResponse(response_html)

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         projects_list_url = reverse('tasks:projects_list')
#         quality_control_index_url = reverse('quality_control:index')
#
#         html = f"<h1>Страница приложения tasks</h1>"
#         html += f"<a href='{projects_list_url}'>Список проектов</a><br>"
#         html += f"<a href='{quality_control_index_url}'>Перейти на главную страницу приложения quality_control</a>"
#
#         return HttpResponse(html)

from django.views.generic import ListView

class ProjectsListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'

# class ProjectsListView(ListView):
#     model = Project
#
#     def get(self, request, *args, **kwargs):
#         projects = self.get_queryset()
#         projects_html = '<h1>Список проектов</h1>'
#
#
#
#         for project in projects:
#             projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#         projects_html += '</ul>'
#         return HttpResponse(projects_html)


from django.views.generic import DetailView

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

# class ProjectDetailView(DetailView):
#     model = Project
#     pk_url_kwarg = 'project_id'
#
#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         project = self.object
#         tasks = project.tasks.all()
#         response_html = f'<h1>{project.name}</h1><p>{project.description}</p>'
#         response_html += '<h2>Задачи</h2><ul>'
#         for task in tasks:
#             response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
#         response_html += '</ul>'
#         return HttpResponse(response_html)

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'

# class TaskDetailView(DetailView):
#     model = Task
#     pk_url_kwarg = 'task_id'
#
#     def get(self, request, *args, **kwargs):
#         task = self.get_object()
#         response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
#         return HttpResponse(response_html)




#from django.http import HttpResponse
#from django.urls import reverse

#def index(request):
#   quality_control_index_url = reverse('quality_control:index')
#    html = f"<h1>Главная страница приложения tasks</h1><a href='{quality_control_index_url}'>Перейти на главную страницу приложения quality_control</a>"
#    return HttpResponse(html)