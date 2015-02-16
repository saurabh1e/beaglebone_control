from django.shortcuts import render
from Adafruit_BBIO import *
import random
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.http import JsonResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from sample.models import *
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import time
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.http import HttpResponse, JsonResponse
from sample.models import *


def main_page(request):
    context = RequestContext(request)
    return render_to_response('base.html', context)

def rooms(request):
    print("gotcha!!")
    context = RequestContext(request)
    room = RoomID.objects.all()
    context_dict = {"room": room}
    return render_to_response('rooms.html', context_dict, context)
