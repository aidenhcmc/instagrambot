import argparse

def get_proxy():
  parser = argparse.ArgumentParser(add_help=True)
  parser.add_argument('-u', type=str, help="username")
  parser.add_argument('-p', type=str, help="password")
  parser.add_argument('-proxy', type=str, help="proxy")
  parser.add_argument('user', type=str, nargs='*', help="user")
  parser.add_argument('-path', type=str, default='', help="path")
  args = parser.parse_args()
  return args.proxy