import json

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from sample.models import *
from django.core import serializers
import serial

def main_page(request):
    context = RequestContext(request)
    return render_to_response('homepage.html', context)


def rooms(request):
    print('gotcha!!')
    context = RequestContext(request)
    room = RoomID.objects.all()
    rooms = serializers.serialize('json', room)
    return HttpResponse(json.dumps(rooms), content_type='application/json')


def appliances(request):
    print('gotcha!!')
    context = RequestContext(request)
    app = Appliances.objects.order_by('roomid').all()
    a = [{'name': a.name, 'id': a.id, 'status': a.status, 'roomid': a.roomid.name} for a in app]
    return HttpResponse(json.dumps(a), content_type='application/json')


def wireless(request):
    print('gotcha!!')
    context = RequestContext(request)
    wireless = Wireless.objects.all()
    wls = serializers.serialize('json', wireless)
    return HttpResponse(json.dumps(wls), content_type='application/json')


def toggle(request, t_id):
    context = RequestContext(request)
    appliance = Appliances.objects.get(id=t_id)
    if t_id == 1:
        ser = serial.Serial(port="dev/ttyUSB0", baudrate=57600)
        ser.write('1')
    if request.method == 'PUT':
        data = json.loads(request.body)
        print data['status']
        if data['status']:
            appliance.status = bool(1)
            appliance.save()
            print ("here 1")
            return HttpResponse(json.dumps("saved"), 200)
        else:
            appliance.status = bool(0)
            appliance.save()
            print ("here 2")
            return HttpResponse(json.dumps("saved"), 200)
    return HttpResponse(json.dumps("unsuccessful"), 403)


