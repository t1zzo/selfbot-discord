import requests
import time
import os
import colorama
from colorama import Fore, Style
import json

colorama.init()

with open("language.txt", "r") as f:
    language = f.read().strip()

if language == "en":
    lang_file = "lang/en.json"
elif language == "pt":
    lang_file = "lang/pt.json"

with open(lang_file, "r") as f:
    messages = json.load(f)

print(f"""{Fore.GREEN}
                        (_).-----------------.(_)
                        /.'                   '.
                        |:    godscript        :|
                        |:  github.com/t1zzo   :|
                        |:                     :|
                        |:                     :|  
                        .'---------------------'.
                      .'                         '.
                    .'-----------------------------'.
                    'lc.............................'
                      \   _____________________   /
                       | |_)                 (_| |
                       | |                     | |
                       | |                     | |
                      (___)                   (___)  """)

print("")
webhook_url = input(messages["input_webhook_url"])
print("---------------------------------------------------")
message = input(messages["input_message"])
print("---------------------------------------------------")
username = input(messages["input_username"])
print("---------------------------------------------------")

msg_count = input(messages["input_msg_count"])
while True:
    try:
        msg_count = int(msg_count)
        if msg_count < 1 or msg_count > 50:
            raise ValueError()
        break
    except ValueError:
        msg_count = input(messages["input_invalid_count"])

payload = {
    "content": message,
    "username": username
}

for i in range(msg_count):
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        if "message_sent" in messages:
            print(messages["message_sent"].replace("{count}", str(msg_count)).replace("{index}", str(i+1)))
        else:
            print(["mensagem_enviada"])
    else:
        if "message_failed" in messages:
            print(messages["message_failed"].replace("{count}", str(msg_count)).replace("{index}", str(i+1)))
        else:
            print(["mensagem_falha"].format(i+1, msg_count))
    time.sleep(0.5)


input(messages["press_enter2"])
