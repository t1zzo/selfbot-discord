import os
import requests
import time
import json
from colorama import Fore
import colorama
colorama.init()


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

print()

web = input(messages["url_prompt"])
print("------------------------------------------------------------")
msg = input(messages["msg_prompt"])
print("------------------------------------------------------------")

# Verifica se o usuário quer incluir @everyone na mensagem
while True:
    everyone = input(messages["everyone_prompt"]).lower()
    print("------------------------------------------------------------")
    if everyone == "y":
        msg += " @everyone"
        break
    elif everyone == "n":
        break
    else:
        print(messages["invalid_option"])

username = input(messages["username_prompt"])
print("------------------------------------------------------------")
spam_times = input(messages["times_prompt"])
print("------------------------------------------------------------")

# Verifica se o usuário digitou um valor numérico válido para a quantidade de mensagens
while True:
    try:
        spam_times = int(spam_times)
        if 1 <= spam_times <= 50:
            break
        else:
            print(messages["invalid_quantity"])
            spam_times = input(messages["times_prompt"])
            print("------------------------------------------------------------")
    except ValueError:
        print(messages["invalid_quantity"])
        spam_times = input(messages["times_prompt"])
        print("------------------------------------------------------------")

webhook_url = f"https://discord.com/api/webhooks/{web.split('/')[-2]}/{web.split('/')[-1]}"
headers = {'Content-Type': 'application/json'}

# Envia a mensagem spam_times vezes
for i in range(spam_times):
    payload = {'username': username, 'content': msg}
    response = requests.post(webhook_url, headers=headers, json=payload)

print(messages["webhook_deleted"])
requests.delete(web)

print("Deletado com sucesso!")
time.sleep(2)



