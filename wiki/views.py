from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.defaults import page_not_found
import markdown2
import os
from encyclopedia import util


def handler404(request, exception):
    return render(request, 'wiki/404.html', status=404)


def title(request, entry):
    file = os.path.join('entries', f'{entry}.md')

    contents = ''
    try:
        with open(file, 'r') as f:
            contents = f.read()
    except FileNotFoundError as fileNotFoundError:
        return handler404(request, fileNotFoundError)

    html = markdown2.markdown(contents)

    return render(request, "wiki/title.html", {
        "content": html,
        "title": entry
    })
