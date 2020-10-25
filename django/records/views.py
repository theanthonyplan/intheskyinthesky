from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Record
import random


# Create your views here.
def random_record(request):
    # from ALL off our records
    records = Record.objects.all()
    # Get a random record
    random_record = random.choice(records)

    template = loader.get_template('records/index.html')
    context = {
        'random_record': random_record,
    }

    return HttpResponse(template.render(context, request))

def detail(request, record_id):
    record = Record.objects.get(pk=record_id)
    response = "You're looking at the record {}.".format(record_id)
    return render(request, 'records/details.html', {"record_details":record})


def vote(request, record_id, is_real):
    record = Record.objects.get(pk=record_id)
    vote_is_real = int(is_real) == 1;

    if vote_is_real is True:
        if record.is_human is True:
            record.correct_count += 1
        else:
            record.incorrect_count += 1
    else:
        if record.is_human is True:
            record.incorrect_count += 1
        else:
            record.correct_count += 1
    record.save()

    return render(request, 'records/details.html', {"record_details":record})
