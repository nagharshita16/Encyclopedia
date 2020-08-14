import markdown2
import random
from django.shortcuts import render
from django import forms
from . import util

class NewTaskForm(forms.Form):
    title = forms.CharField(label = "Enter title")
    text = forms.CharField(widget=forms.Textarea, label="text")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def display(request, name):
    if name == "K":
        choice = random.choice(util.list_entries())
        return render(request, "encyclopedia/display.html", {
        "content": markdown2.markdown(util.get_entry(choice)),
        })
    if name in util.list_entries():
        return render(request, "encyclopedia/display.html", {
        "content": markdown2.markdown(util.get_entry(name)),
        })

        
def createNewEntry(request):
    if request.method == "GET":
        return render(request, "encyclopedia/createNewEntry.html", {
        "form":NewTaskForm()
        })    

    elif request.method == "POST":
            form = NewTaskForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]
                text = form.cleaned_data["text"]
                util.save_entry(title,text)
            return render(request, "encyclopedia/display.html", {
            "content": markdown2.markdown(util.get_entry(title)),
            }) 
            return render(request, "encyclopedia/createNewEntry.html", {
            "form": form
             })           
            
            



