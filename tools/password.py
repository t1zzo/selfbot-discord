import os
import time
import random , string
import json


os.system("cls")

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
                               .-~ | ~-.
                               |   |   |
                               |  _:_  |                    .-:~--.._
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |      |
  _..--~:-.|    |  |         |     |     |                |   |      |
 |      |  ~.   |  |         |  __.:.__  |                |   |      |
 |      |   |   |  |       .-"~~   |   ~~"-.              |   |      |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |          | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |          | |      |   | |       |  |   |     |  |  |   |   |      |
 |          | |      |   | |       |  |   |     |  |  |   |   |      |
 |          | |      |   | |       |  |   |     |  |  |   |   |      |
 |          | |      |   | |       |  |   |     |  |  |   |   |      |
 |          | |      |   | |       |  |   |     |  |  |   |   |      | """)

time.sleep(2)

amount_letters = int(input(messages["input_amount_letters"]))
amount_passwords = int(input(messages["input_amount_passwords"]))

for i in range(amount_passwords):
    code = "".join(random.choices(string.ascii_letters + string.digits, k=amount_letters))
    with open("Password.txt", "a+") as f:
        f.write(f"{code}\n")
    print(messages["generated_password"].format(password=code))
