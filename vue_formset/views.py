import json

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import forms
from . import models


def index(request):
    return render(request, 'index.html', {})


def get_persons(request):
    return JsonResponse({
        "results": [
            {
                "id": p.id,
                "name": p.name,
                "age": p.age,
                "is_active": p.is_active,
                "status": None,
                "birthday": p.birthday.strftime("%Y-%m-%d")
            } for p in models.Person.objects.all()
        ]
    })


@csrf_exempt
def update_persons(request):
    content = json.loads(request.body.decode("utf-8"))

    for row in content:

        form = forms.PersonForm(row)
        if not form.is_valid():
            continue

        id = form.cleaned_data["id"]
        if id is not None:
            person = models.Person.objects.get(id=form.cleaned_data["id"])
            if form.cleaned_data.get("status") == 'delete':
                # delete
                person.delete()
            else:
                # update
                person.name = form.cleaned_data["name"]
                person.age = form.cleaned_data["age"]
                person.is_active = form.cleaned_data["is_active"]
                person.birthday = form.cleaned_data["birthday"]
                person.save()
        else:
            # add
            models.Person.objects.create(
                name=form.cleaned_data["name"],
                age=form.cleaned_data["age"],
                is_active=form.cleaned_data["is_active"],
                birthday=form.cleaned_data["birthday"]
            )

    return JsonResponse({})
