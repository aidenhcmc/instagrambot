from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .helper.utils import *
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

    login_response = Bot().login(username=username, password=password,  proxy=get_proxy())
    if login_response is not None:
      logged_account = login_response['logged_in_user']
      full_name = logged_account['full_name']
      profile_pic_url = logged_account['profile_pic_url']
      profile_pic_id = logged_account['profile_pic_id']
      phone_number = logged_account['phone_number']

      account = Account(username=username, password=password, full_name=full_name, profile_pic_url=profile_pic_url, profile_pic_id=profile_pic_id, phone_number=phone_number)
      account.save()
      account.user.add(request.user)
      response_data['status'] = True
    else:
      response_data['status'] = False

    return HttpResponse(
      json.dumps(response_data),
      content_type="application/json"
    )
  else:
    return HttpResponse(
      json.dumps({"status": False}),
      content_type="application/json"
    )
  # print(bot.get_user_info('1333985159'))

  try:
      ua = request.META['HTTP_USER_AGENT']
  except KeyError:
      ua = 'unknown'
  return HttpResponse("Your browser is %s" % request.POST['username'])
