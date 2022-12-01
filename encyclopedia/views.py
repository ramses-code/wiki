from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def convert(file_name):
    markdowner = Markdown()
    return markdowner.convert(file_name)

def get_entry(request, title):
    result = util.get_entry(title)

    if result == None:
        return render(request, 'encyclopedia/error.html', {
            'code': 404,
            'msg': 'Page not found'
        })

    return render(request, 'encyclopedia/entry.html', {
        'title': title,
        'entry': convert(result)
    })

def search(request):
    if request.method == 'POST':
        search_entry = request.POST['q']
        entry_page = util.get_entry(search_entry)
        
        if entry_page:
            return render(request, 'encyclopedia/entry.html', {
                'title': search_entry,
                'entry': convert(entry_page)
            })
        else:
            return render(request, 'encyclopedia/search.html', {
                "sub_string": search_entry,
                "entries": util.list_entries()
            })

def new_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        entry = util.get_entry(title)
        if entry == None:
            util.save_entry(title, content)
            entry = util.get_entry(title)
            return render(request, 'encyclopedia/entry.html', {
                'title': title,
                'entry': convert(entry)
            })
        else:
            return render(request, 'encyclopedia/error.html', {
            'msg': 'Entry already exist'
        })

    return render(request, 'encyclopedia/new_entry.html')

def edit_page(request):
    title = request.POST['entry_title']
    entry = util.get_entry(title)

    return render(request, 'encyclopedia/edit.html', {
        'title': title,
        'content': entry
    })

def save_page(request):
    new_title = request.POST['new_title']
    new_content = request.POST['new_content']

    util.save_entry(new_title, new_content)
    return render(request, 'encyclopedia/entry.html', {
        'title': new_title,
        'entry': convert(new_content)
    })

def random_page(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    entry = util.get_entry(random_title)
    return render(request, 'encyclopedia/entry.html', {
        'title': random_title,
        'entry': convert(entry)
    })
