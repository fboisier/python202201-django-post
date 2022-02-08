import pdb
import sys
import os
import fileinput


text_index = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    {% load static %}
    {{ saludo }}
    <script src="{% static 'js/index.js' %}"></script>
</body>
</html>
'''


def add_after(filename, old_line, new_line, esReemplazo=False):
    with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
        for line in f:
            if old_line in line:
                if esReemplazo:
                    print(new_line)
                else:
                    print(line +  new_line, end='\n')
            else:
                print(line, end='')


def create_app(project, app):
    os.chdir(project)
    os.system(f'python manage.py startapp {app}')
    add_after(f'{project}/settings.py', 'INSTALLED_APPS', f"    '{app}',")
    add_after(f'{project}/settings.py', f"LANGUAGE_CODE = 'en-us'", f"LANGUAGE_CODE = 'es'", True)
    add_after(f'{project}/settings.py', f"TIME_ZONE = 'UTC'", f"TIME_ZONE = 'America/Santiago'", True)
    add_after(f'{project}/urls.py', 'from django.urls', 'from django.urls import include')
    add_after(
        f'{project}/urls.py',
        'urlpatterns = [',
        f"    path('', include('{app}.urls')),")
    
    lines_url = [
        'from django.urls import path',
        'from . import views',
        "urlpatterns = [",
        "    path('', views.index),",
        "    path('second/<name>', views.second)",
        "]"
    ]
    f = open(f'{app}/urls.py', 'w')
    for line in lines_url:
        f.write(line)
        f.write('\n')
    f.close()

    lines_views = [
        'from django.shortcuts import render, HttpResponse',
        '',
        'def index(request):',
        "    context = {",
        "        'saludo': 'Hola'",
        "    }",
        "    return render(request, 'index.html', context)",
        '',
        '',
        'def second(request, name):',
        "    return HttpResponse('Hola ' + name)",
        ''
    ]
    f = open(f'{app}/views.py', 'w')
    for line in lines_views:
        f.write(line)
        f.write('\n')
    f.close()

    os.makedirs(f'{app}/templates')
    f = open(f'{app}/templates/index.html', 'w')
    f.write(text_index)
    f.close()

    os.makedirs(f'{app}/static')
    os.makedirs(f'{app}/static/js')
    f = open(f'{app}/static/js/index.js', 'w')
    f.write('// js code\n')
    f.close()


def main():
    if len(sys.argv) < 3:
        print('Usage error')
        sys.exit()
    project = sys.argv[1]
    app = sys.argv[2]
    if not os.path.exists(project):
        os.system(f'django-admin startproject {project}')

    create_app(project, app)


if __name__ == '__main__':
    main()
