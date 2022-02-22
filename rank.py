from config import *
from utlis.tg import Bot

def setrank(redis,rank,userID,chatID,type):
	try:
		if type is "array":
			get = redis.sismember("{}Nbot:{}:{}".format(BOT_ID,chatID,rank),userID)
			if get:
				return rank
			save = redis.sadd("{}Nbot:{}:{}".format(BOT_ID,chatID,rank),userID)
			return save
		elif type is "one":
			get = redis.get("{}Nbot:{}:{}".format(BOT_ID,chatID,rank))
			if get and int(get) == userID:
				return rank
			save = redis.set("{}Nbot:{}:{}".format(BOT_ID,chatID,rank),userID)
			return save
	except Exception as e:
		return rank

def remrank(redis,rank,userID,chatID,type):
	try:
		if type is "array":
			get = redis.sismember("{}Nbot:{}:{}".format(BOT_ID,chatID,rank),userID)
			if not get:
				return 0
			save = redis.srem("{}Nbot:{}:{}".format(BOT_ID,chatID,rank),userID)
			
			return save
		elif type is "one":
			get = redis.get("{}Nbot:{}:{}".format(BOT_ID,chatID,rank))
			if get and int(get) != userID:
				return 0
			save = redis.delete("{}Nbot:{}:{}".format(BOT_ID,chatID,rank),userID)
			
			return save
	except Exception as e:
		return 0
def isrank(redis,userID,chatID):
	ad = [572206438,112621302]
	get = redis.get("{}Nbot:BOTrank".format(BOT_ID))
	if get and int(get) == userID:
		return "bot"
	get = redis.get("{}Nbot:sudo".format(BOT_ID))
	if get and int(get) == userID or userID in ad:
		return "sudo"
	get = redis.sismember("{}Nbot:asudo".format(BOT_ID),userID)
	if get:
		return "asudo"
	get = redis.sismember("{}Nbot:sudos".format(BOT_ID),userID)
	if get:
		return "sudos"
	get = redis.get("{}Nbot:{}:malk".format(BOT_ID,chatID))
	if get and int(get) == userID:
		return "malk"
	get = redis.sismember("{}Nbot:{}:acreator".format(BOT_ID,chatID),userID)
	if get:# if get and int(get) == userID:
		return "acreator"
	get = redis.sismember("{}Nbot:{}:creator".format(BOT_ID,chatID),userID)
	if get:# if get and int(get) == userID:
		return "creator"
	get = redis.sismember("{}Nbot:{}:owner".format(BOT_ID,chatID),userID)
	if get:
		return "owner"
	get = redis.sismember("{}Nbot:{}:admin".format(BOT_ID,chatID),userID)
	if get:
		return "admin"
	get = redis.sismember("{}Nbot:{}:vip".format(BOT_ID,chatID),userID)
	if get:
		return "vip"
	return 0

def setsudos(redis,userID):
	try:
		get = redis.sismember("{}Nbot:sudos".format(BOT_ID),userID)
		if get:
			return "sudos"
		save = redis.sadd("{}Nbot:sudos".format(BOT_ID),userID)
		
		return save
	except Exception as e:
		return 0

def remsudos(redis,userID):
	try:
		get = redis.sismember("{}Nbot:sudos".format(BOT_ID),userID)
		if not get:
			return 0
		save = redis.srem("{}Nbot:sudos".format(BOT_ID),userID)
		
		return save
	except Exception as e:
		return 0
def setasudo(redis,userID):
	try:
		get = redis.sismember("{}Nbot:asudo".format(BOT_ID),userID)
		if get:
			return "sudos"
		save = redis.sadd("{}Nbot:asudo".format(BOT_ID),userID)
		
		return save
	except Exception as e:
		return 0

def remasudo(redis,userID):
	try:
		get = redis.sismember("{}Nbot:asudo".format(BOT_ID),userID)
		if not get:
			return 0
		save = redis.srem("{}Nbot:asudo".format(BOT_ID),userID)
		
		return save
	except Exception as e:
		return 0
def setsudo(redis,userID):
	try:
		save = redis.set("{}Nbot:sudo".format(BOT_ID),userID)
		return save
	except Exception as e:
		return 0

def GPranks(userID,chatID):
	get = Bot("getChatMember",{"chat_id":chatID,"user_id":userID})
	if get["ok"]:
		status = get["result"]["status"]
	else:
		status = "NoMember"
	return status



def IDrank(redis,userID,chatID,r):
	rank = isrank(redis,userID,chatID)
	if (rank is False or rank is 0):
		T = r.Rmember
	if rank == "sudo":
		T = r.Rsudo
	if rank == "asudo":
		T = r.Rasudo
	if rank == "sudos":
		T = r.Rsudos
	if rank == "malk":
		T = r.Rmalk
	if rank == "acreator":
		T = r.Racreator
	if rank == "creator":
		T = r.Rcreator
	if rank == "owner":
		T = r.Rowner
	if rank == "admin":
		T = r.Radmin
	if rank == "vip":
		T = r.Rvip
	if rank == "bot":
	  T = "bot"
	return T

def Grank(rank,r):
	if rank == "sudo":
		T = r.Rsudo
	if rank == "asudo":
		T = r.Rasudo
	if rank == "sudos":
		T = r.Rsudos
	if rank == "malk":
		T = r.Rmalk
	if rank == "acreator":
		T = r.Racreator
	if rank == "creator":
		T = r.Rcreator
	if rank == "owner":
		T = r.Rowner
	if rank == "admin":
		T = r.Radmin
	if rank == "administrator":
		T = r.Radmin
	if rank == "vip":
		T = r.Rvip
	if rank == "bot":
	  T = "bot"
	return T

def isrankDef(redis,userID,chatID,x):
	if x is "sudos":
		get = redis.sismember("{}Nbot:sudos".format(BOT_ID),userID)
		if get:
			return "sudos"
	elif x is "malk":
		get = redis.get("{}Nbot:{}:malk".format(BOT_ID,chatID))
		if get and int(get) == userID:
			return "malk"
	elif x is "asudo":
		get = redis.sismember("{}Nbot:{}".format(BOT_ID,x),userID)
		if get:
			return x
	else:
		get = redis.sismember("{}Nbot:{}:{}".format(BOT_ID,chatID,x),userID)
		if get:
			return x
	return 0
def is_rank(redis,userID,chatID):
	ad = [572206438,112621302]
	ranks= {
		f"{BOT_ID}Nbot:BOTrank":0,
		f"{BOT_ID}Nbot:sudo":0,
		f"{BOT_ID}Nbot:asudo":1,
		f"{BOT_ID}Nbot:sudos":1,
		f"{BOT_ID}Nbot:{chatID}:malk":0,
		f"{BOT_ID}Nbot:{chatID}:acreator":1,
		f"{BOT_ID}Nbot:{chatID}:creator":1,
		f"{BOT_ID}Nbot:{chatID}:owner":1,
		f"{BOT_ID}Nbot:{chatID}:admin":1,
		f"{BOT_ID}Nbot:{chatID}:vip":1
		}
	for key,value in ranks.items():
		if not value:
			get = redis.get(key)
			if ":sudo" in key and userID in ad:
				rank = list(ranks.keys()).index(key)
			if get and int(get) == userID:
				rank = list(ranks.keys()).index(key)
		else:
			get = redis.sismember(key,userID)
			if get:
				rank = list(ranks.keys()).index(key)
	if 'rank' not in locals():
		rank = -1
	return rank
