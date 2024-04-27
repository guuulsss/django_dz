#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_tracker.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    from quality_control.models import BugReport

    BugReport.objects.create(
        title='1',
        status='New',
        description='Кнопка на главной странице не работает'
    )

    BugReport.objects.create(
        title='Ошибка в аутентификации',
        status='In progress',
        description='Пользователи не могут войти в систему'
    )

    BugReport.objects.create(
        title='Проблемы с отображением',
        status='Completed',
        description='Страница отображается неправильно на мобильных устройствах'
    )


if __name__ == '__main__':
    main()
