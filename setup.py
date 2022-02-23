import requests,os

try:
  from config import *
  os.system('pm2 start bot.py --name {} --interpreter python3.8 --interpreter-args -u'.format(BOT_ID))
except Exception as e:
  API_ID = 793178
  API_HASH = '9f4461079f30757ca0a4c23e14bd523f'

  out ="""
API_ID = 793178
API_HASH = '9f4461079f30757ca0a4c23e14bd523f'
"""
  def Bot(TOKEN,method,data):
    url = "https://api.telegram.org/bot{}/{}".format(TOKEN,method)
    post = requests.post(url,data=data)
    return post.json()
  ID = ""
  go = True
  while go:
    token = input("أدخل توكن bot خاص بك:")
    get = Bot(token,"getme",{})
    if get["ok"]:
      out = out+"\n"+"TOKEN = '{}'\nBOT_ID = TOKEN.split(':')[0]".format(token)
      go = False
      ID = token.split(':')[0]

    else:
      print("توكن غير صحيح، حاول مرة اخرى ")

  sudo = input("أدخل ايدي خاص بك:")
  out = out+"\n"+"SUDO = {}".format(sudo)
  botate = input("أدخل معرف قناتك: @")
  out = out+"\n"+"BOTATE = '{}'".format(botate)

  f = open("config.py","w+") 
  f.write(out)
  f.close()

  os.system('pm2 start bot.py -f --name {} --interpreter python3.8 --interpreter-args -u'.format(ID))
