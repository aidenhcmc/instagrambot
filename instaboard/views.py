from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .utils import *
from .models import Account

from tools import Bot

import json

@login_required
def index(request):
  if not request.user.is_authenticated:
    return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

  context = {
    'latest_account': Account.objects.filter(user=request.user),
  }
  return render(request, 'index.html', context)

@csrf_exempt
def account(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    response_data = {}
    
    Bot().login(username=username, password=password,  proxy=get_proxy())
    
    return HttpResponse(
      json.dumps(response_data),
      content_type="application/json"
    )
  else:
    return HttpResponse(
      json.dumps({"nothing to see": "this isn't happening"}),
      content_type="application/json"
    )
  # print(bot.get_user_info('1333985159'))

  try:
      ua = request.META['HTTP_USER_AGENT']
  except KeyError:
      ua = 'unknown'
  return HttpResponse("Your browser is %s" % request.POST['username'])
