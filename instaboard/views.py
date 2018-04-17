from django.shortcuts import render
from django.http import HttpResponse

from tools import Bot
import argparse


def index(request):
    bot = Bot()

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-u', type=str, help="username")
    parser.add_argument('-p', type=str, help="password")
    parser.add_argument('-proxy', type=str, help="proxy")
    parser.add_argument('user', type=str, nargs='*', help="user")
    parser.add_argument('-path', type=str, default='', help="path")
    args = parser.parse_args()

    # bot.login(username='chabong.bong', password='Stop@here',  proxy=args.proxy)

    # print(bot.get_user_info('1333985159'))
    return render(
      request,
      'index.html',
    )
