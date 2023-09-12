import random

from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from encyclopedia import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request):
    query = request.GET.get('q', '')
    entries = util.list_entries()
    matches = [entry for entry in entries if query.lower() in entry.lower()]

    if query in entries:
        return redirect(reverse('wiki:title', args=[query]))
    else:
        return render(request, 'encyclopedia/search_results.html', {
            "query": query,
            "entries": matches
        })


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    entry = forms.CharField(widget=forms.Textarea)


def create_page(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            entry = form.cleaned_data['entry']

        entries = util.list_entries()

        if title in entries:
            error = 'The page with that entry name already exists. Please try again'
            return render(request, 'encyclopedia/create_page.html', {'error': error, 'form': form})
        else:
            util.save_entry(title, entry)
            return redirect('wiki:index')
    else:
        form = NewEntryForm()
    return render(request, 'encyclopedia/create_page.html', {'form': form})


class EditForm(forms.Form):
    entry = forms.CharField(widget=forms.Textarea)


def edit_page(request, title):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data['entry']
            util.save_entry(title, entry)
            return redirect('wiki:title', title)
    else:
        form = EditForm(initial={'entry': util.get_entry(title)})
    return render(request, 'encyclopedia/edit_page.html', {
        'form': form,
        'title': title
    })


def random_page(request):

    l = util.list_entries()
    items = len(l)
    random_index = random.randrange(items)
    title = l[random_index]
    print(title)
    return redirect('wiki:title', title)
