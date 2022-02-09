# the tool made by : Leaks station#3384 / @leaks_station
from requests import get
import json
import time
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import tweepy
#######################################################################
with open ("yourTokens.json" , "r+") as token :
    tokens = json.load(token)
#TOKENS OF ALL [TWITTER]
consumer_key = tokens['data']['API_key'] #TWITTER
consumer_secret_key = tokens['data']['API_Secret_Key'] #TWITTER
access_token = tokens['data']['Access_Token'] #TWITTER
access_token_secret = tokens['data']['Access_Token_Secret'] #TWITTER
if consumer_key == "" or consumer_secret_key == "" or access_token == "" or access_token_secret == "" : print(f"{Fore.RED}-> Please Check Your Tokens in [youtTokens.json]- missing token !!"),time.sleep(5),exit()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweeting(Readfortweet,text="-> New Hotfix Tweeted successfully"):
  try: api.update_status(Readfortweet),print(f"{Fore.BLUE}{text}\n\n")
  except: print(f"{Fore.RED}-> Failed to tweet")
#######################################################################
def Bot():
  Tweet = False
  data = get("https://benbot.app/api/v1/hotfixes").json()[""]
  Odata = open("data/oldhotfixes.json","r+")
  olddata = json.load(Odata)
  if data == {} or data == None :
    print(f"{Fore.RED} Not checking The Api is Empty ( The bot will start Checking again when the api back) ".title())
  elif data == olddata :
    print(f"{Fore.LIGHTGREEN_EX}>>> Searching For New Hotfix!")
  else:
    ReadfortweetNew = "New Hotfixes: \n"
    print(f"{Fore.CYAN}-> New Hotfix Detected !!!")
    for i in data :
      if i not in olddata : 
        Tweet = i not in olddata
        print(f"New Hotfix : {Fore.LIGHTYELLOW_EX}-> ID :{i}")
        dataget = data[i] 
        ReadfortweetNew = ReadfortweetNew + f"• {dataget}\n"
    #To tweet every single one Because we can tweet all of them one time , due to the max limit of twtter 280 character ONLY
    if len(ReadfortweetNew) > 280 :
      for i in data :
        ReadfortweetNew = "New Hotfixes: \n"
        if i not in olddata :
          dataget = data[i] 
          ReadfortweetNew = ReadfortweetNew + f"• {dataget}\n"
          print(f"New Hotfix : {Fore.LIGHTYELLOW_EX}-> ID :{i}")
          tweeting(Readfortweet=ReadfortweetNew)
    #Here will make sure if it's Equal or Less the the Limit Of twitter , iF less than the limit, It will post it all in one tweet
    elif len(ReadfortweetNew) <= 280 :
      if Tweet == True :
        tweeting(Readfortweet=ReadfortweetNew)
    #Here Checking for new Modification Of any Hotix :D
    for i in data :
      if i in olddata :
        ReadfortweetModification = "New Hotfix Modification : \n"
        if olddata[i] != data[i] :
          print(f"{Fore.LIGHTCYAN_EX}-> Hotfix Modification Detected !!!\n ID : {i}\n{Fore.LIGHTYELLOW_EX}-> OLD : {olddata[i]}\n{Fore.YELLOW}-> NEW : {data[i]}")
          ReadfortweetModification = ReadfortweetModification + f"ID: {i} \n\nOLD: {olddata[i]}\n\nNew: {data[i]}\n\n\n"
          tweeting(Readfortweet=ReadfortweetModification,text="-> Hotfix Modification Tweeted successfully")
    Odata = open("data/oldhotfixes.json","w+")
    json.dump(data,Odata,indent=3)

if "HI"== "HI":
  while True:
    try:
      Bot()
    except:
      print(f"{Fore.LIGHTRED_EX}-> ERROR [INTERNET PROBLEM/ELSE (the bot will stop detecting until the error stop)]")
    time.sleep(20)
