import os, sys, json
import django
import random

# set some env vars
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ufo.settings")

def populate_fake_records(count=60):
    print("Populating database with {} fake records.".format(count))
    records = []

    for line in open('fake_data.txt', 'r'):
        # now we are going to go through and load each line as json
        # and we will appaend it to our data list
        records.append(line)
        # print(line)
        # input()
    # make it a little more random
    random.shuffle(records)
    for record_number in range(count):
        print(record_number)
        print(records[record_number])
        # print(type(records))
        # print(len(records))

        Record.objects.get_or_create(summary=records[record_number], is_human=False)
        # input()

def populate_real_records(count=60):
    print("Populating database with {} real records.".format(count))

    records = []

    for line in open('real_records.txt', 'r'):
        # now we are going to go through and load each line as json
        # and we will appaend it to our data list
        records.append(line)
        # print(line)
        # input()
    # make it a little more random
    random.shuffle(records)
    for record_number in range(count):
        print(record_number)
        print(records[record_number])
        # print(type(records))
        # print(len(records))

        Record.objects.get_or_create(summary=records[record_number], is_human=True)
        # input()



if __name__ == '__main__':
    records_count = 60
    records_real = True

    # how many records should we set?  passed as a script arg
    arg1 = None
    if  len(sys.argv) > 1:
        arg1 =  sys.argv[1]

    if arg1 is not None:
        if int(arg1) > 0:
            records_count = arg1

    # should we use real records or fake ones?
    arg2 = None
    if len(sys.argv) > 2:
        arg2 = sys.argv[2]
        if arg2 == 'Fake' or arg2 == 'fake':
            records_real = False

    # get django ready
    django.setup()
    #import our django models
    from records.models import Record

    print(records_count, records_real)
    print(Record)

    if records_real is False:
        populate_fake_records(int(records_count))
    else:
        populate_real_records(int(records_count))



    # # e.g. add a new location
    # l = Location()
    # l.name = 'Berlin'
    # l.save()
    #
    # # this is an example to access your model
    # locations = Location.objects.all()
    # print locations
    #
    # # e.g. delete the location
    # berlin = Location.objects.filter(name='Berlin')
    # print berlin
    # berlin.delete()
