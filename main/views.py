from django.shortcuts import render, redirect
from .forms import Testform
from .models import Testmodel
import json


def get(request):
    if request.method == 'POST':
        form = Testform(request.POST)
        if form.is_valid():
            name_input = form.cleaned_data['testfield']
            data = json.dumps(name_input, ensure_ascii=False)
            Testmodel.objects.create(data=data, field='testfield')
            for count in range(1, len(request.POST) - 1):
                query = 'field' + str(count)
                input_value = request.POST[query]
                if input_value:
                    data = json.dumps(input_value, ensure_ascii=False)
                    field = json.dumps(query)
                    Testmodel.objects.create(data=data, field=field)
                count += 1
        return redirect('/fine/')
    else:
        form = Testform()
    return render(request, 'base.html', {'form': form})


def fine(request):
    # Take data from the db
    query = Testmodel.objects.all().values('id', 'data', 'field')
    json_list = list(query)
    return render(request, 'fine.html', {'json_list': json_list})
